from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.ai.assistant import analyze_customer_issue

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


class TicketCreate(BaseModel):
    customer: str
    issue: str
    priority: str = "Medium"


class IssueAnalyze(BaseModel):
    customer_name: str
    issue: str


tickets = [
    {
        "id": 1,
        "customer": "Ahmed",
        "issue": "Payment failed",
        "priority": "High",
        "status": "Pending"
    },
    {
        "id": 2,
        "customer": "Rahul",
        "issue": "Login problem",
        "priority": "Medium",
        "status": "Resolved"
    },
    {
        "id": 3,
        "customer": "Sara",
        "issue": "Account access issue",
        "priority": "Low",
        "status": "Pending"
    }
]


@router.get("/")
def get_tickets():
    return tickets


@router.post("/")
def create_ticket(ticket: TicketCreate):
    new_ticket = {
        "id": max([t["id"] for t in tickets], default=0) + 1,
        "customer": ticket.customer,
        "issue": ticket.issue,
        "priority": ticket.priority,
        "status": "Pending"
    }

    tickets.append(new_ticket)
    return new_ticket


@router.patch("/{ticket_id}/resolve")
def resolve_ticket(ticket_id: int):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["status"] = "Resolved"
            return ticket

    raise HTTPException(
        status_code=404,
        detail="Ticket not found"
    )


@router.post("/analyze")
def analyze_issue(data: IssueAnalyze):
    try:
        return analyze_customer_issue(
            data.customer_name,
            data.issue
        )
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"AI analysis failed: {str(error)}"
        )