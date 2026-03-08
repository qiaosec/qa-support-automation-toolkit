from collections import Counter, defaultdict
from dataclasses import asdict
import json
import re

from .loader import load_tickets
from .models import ScoredTicket, Ticket


PRIORITY_WEIGHT = {
    "critical": 40,
    "high": 28,
    "medium": 16,
    "low": 8,
}

TIER_WEIGHT = {
    "enterprise": 18,
    "business": 10,
    "standard": 4,
}

KEYWORD_WEIGHT = {
    "login": 6,
    "export": 6,
    "billing": 5,
    "slow": 4,
    "error": 4,
    "blank": 5,
    "retry": 3,
}


def _keywords(text: str) -> set[str]:
    tokens = re.findall(r"[a-z0-9]+", text.lower())
    return {token for token in tokens if len(token) > 2}


def _title_similarity(left: Ticket, right: Ticket) -> float:
    left_tokens = _keywords(left.title)
    right_tokens = _keywords(right.title)
    if not left_tokens or not right_tokens:
        return 0.0
    union = left_tokens | right_tokens
    overlap = left_tokens & right_tokens
    return len(overlap) / len(union)


def score_ticket(ticket: Ticket) -> int:
    score = PRIORITY_WEIGHT.get(ticket.priority, 16)
    score += TIER_WEIGHT.get(ticket.customer_tier, 4)
    score += min(ticket.created_days_ago, 14)

    haystack = f"{ticket.title} {ticket.description}".lower()
    for keyword, weight in KEYWORD_WEIGHT.items():
        if keyword in haystack:
            score += weight

    if ticket.status == "resolved":
        score -= 18

    return max(score, 0)


def sla_risk(score: int, ticket: Ticket) -> str:
    if ticket.status == "resolved":
        return "low"
    if score >= 65:
        return "high"
    if score >= 40:
        return "medium"
    return "low"


def duplicate_groups(tickets: list[Ticket]) -> dict[str, str]:
    groups: dict[str, str] = {}
    counter = 1
    for index, ticket in enumerate(tickets):
        if ticket.ticket_id in groups:
            continue
        for other in tickets[index + 1 :]:
            if other.ticket_id in groups:
                continue
            if ticket.category == other.category and _title_similarity(ticket, other) >= 0.4:
                group_id = groups.get(ticket.ticket_id)
                if group_id is None:
                    group_id = f"DUP-{counter:03d}"
                    counter += 1
                    groups[ticket.ticket_id] = group_id
                groups[other.ticket_id] = group_id
    return groups


def analyze_tickets(path: str) -> dict:
    tickets = load_tickets(path)
    dup_groups = duplicate_groups(tickets)

    scored: list[ScoredTicket] = []
    for ticket in tickets:
        urgency = score_ticket(ticket)
        scored.append(
            ScoredTicket(
                ticket=ticket,
                urgency_score=urgency,
                sla_risk=sla_risk(urgency, ticket),
                duplicate_group=dup_groups.get(ticket.ticket_id),
            )
        )

    scored.sort(key=lambda item: item.urgency_score, reverse=True)
    top_risks = scored[:5]

    duplicate_index: dict[str, list[str]] = defaultdict(list)
    for item in scored:
        if item.duplicate_group:
            duplicate_index[item.duplicate_group].append(item.ticket.ticket_id)

    categories = Counter(item.ticket.category for item in scored)
    regression_candidates = [
        {
            "category": category,
            "reason": f"{count} recurring tickets in category '{category}'"
        }
        for category, count in categories.items()
        if count >= 2
    ]

    return {
        "summary": {
            "ticket_count": len(scored),
            "open_ticket_count": sum(1 for item in scored if item.ticket.status != "resolved"),
            "high_risk_count": sum(1 for item in scored if item.sla_risk == "high"),
            "duplicate_group_count": len(duplicate_index),
        },
        "top_risks": [
            {
                "ticket_id": item.ticket.ticket_id,
                "title": item.ticket.title,
                "urgency_score": item.urgency_score,
                "sla_risk": item.sla_risk,
                "duplicate_group": item.duplicate_group,
            }
            for item in top_risks
        ],
        "duplicates": duplicate_index,
        "regression_candidates": regression_candidates,
        "tickets": [
            {
                **asdict(item.ticket),
                "urgency_score": item.urgency_score,
                "sla_risk": item.sla_risk,
                "duplicate_group": item.duplicate_group,
            }
            for item in scored
        ],
    }


def to_json_report(report: dict) -> str:
    return json.dumps(report, indent=2, ensure_ascii=False)


def to_markdown_report(report: dict) -> str:
    lines = [
        "# Support Ops Report",
        "",
        "## Summary",
        "",
        f"- Ticket count: {report['summary']['ticket_count']}",
        f"- Open tickets: {report['summary']['open_ticket_count']}",
        f"- High SLA risk tickets: {report['summary']['high_risk_count']}",
        f"- Duplicate groups: {report['summary']['duplicate_group_count']}",
        "",
        "## Top Risks",
        "",
    ]

    for item in report["top_risks"]:
        lines.append(
            f"- {item['ticket_id']} | {item['title']} | score={item['urgency_score']} | risk={item['sla_risk']} | duplicate={item['duplicate_group'] or 'none'}"
        )

    lines.extend(["", "## Duplicate Groups", ""])
    if report["duplicates"]:
        for group_id, ticket_ids in report["duplicates"].items():
            lines.append(f"- {group_id}: {', '.join(ticket_ids)}")
    else:
        lines.append("- None")

    lines.extend(["", "## QA Regression Checklist Candidates", ""])
    if report["regression_candidates"]:
        for item in report["regression_candidates"]:
            lines.append(f"- {item['category']}: {item['reason']}")
    else:
        lines.append("- No recurring categories detected")

    return "\n".join(lines)
