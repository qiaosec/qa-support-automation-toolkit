import csv
import json
from pathlib import Path

from .models import Ticket


def normalize_priority(value: str) -> str:
    value = (value or "").strip().lower()
    mapping = {
        "p0": "critical",
        "p1": "high",
        "p2": "medium",
        "p3": "low",
        "urgent": "critical",
    }
    if value in {"critical", "high", "medium", "low"}:
        return value
    return mapping.get(value, "medium")


def normalize_status(value: str) -> str:
    value = (value or "").strip().lower()
    if value in {"resolved", "closed", "done"}:
        return "resolved"
    if value in {"in_progress", "in progress", "working"}:
        return "in_progress"
    return "open"


def _ticket_from_mapping(item: dict) -> Ticket:
    return Ticket(
        ticket_id=str(item["ticket_id"]),
        title=str(item["title"]).strip(),
        description=str(item.get("description", "")).strip(),
        priority=normalize_priority(item.get("priority", "")),
        status=normalize_status(item.get("status", "")),
        customer_tier=str(item.get("customer_tier", "standard")).strip().lower(),
        created_days_ago=int(item.get("created_days_ago", 0)),
        category=str(item.get("category", "general")).strip().lower(),
    )


def load_tickets(path: str | Path) -> list[Ticket]:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    if file_path.suffix.lower() == ".csv":
        with file_path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            return [_ticket_from_mapping(row) for row in reader]

    if file_path.suffix.lower() == ".json":
        payload = json.loads(file_path.read_text(encoding="utf-8"))
        if not isinstance(payload, list):
            raise ValueError("JSON input must be a list of ticket objects.")
        return [_ticket_from_mapping(row) for row in payload]

    raise ValueError("Supported input formats: .csv and .json")
