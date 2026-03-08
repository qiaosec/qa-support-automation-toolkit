from dataclasses import dataclass


@dataclass(slots=True)
class Ticket:
    ticket_id: str
    title: str
    description: str
    priority: str
    status: str
    customer_tier: str
    created_days_ago: int
    category: str


@dataclass(slots=True)
class ScoredTicket:
    ticket: Ticket
    urgency_score: int
    sla_risk: str
    duplicate_group: str | None
