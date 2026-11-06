import json
import ollama


def analyze_customer_issue(customer_name: str, issue: str):

    issue_lower = issue.lower()

    response = ollama.chat(
        model="llama3.2",
        format="json",
        messages=[
            {
                "role": "system",
                "content": """
                You are SupportPilot AI, a professional customer
                support assistant.

                Analyze the customer's issue and return valid JSON.

                Required fields:
                category,
                priority,
                suggested_reply,
                recommended_solution.

                Priority must be High, Medium, or Low.

                Give professional replies and practical solutions.
                Never invent contact details.
                Never promise refunds or guaranteed outcomes.
                Use simple English.
                """
            },
            {
                "role": "user",
                "content": f"""
                Customer Name: {customer_name}
                Customer Issue: {issue}
                """
            }
        ],
        options={"temperature": 0.2}
    )

    result = json.loads(response.message.content)

    # Python-based priority validation
    high_priority_keywords = [
        "money deducted",
        "money was deducted",
        "amount deducted",
        "payment deducted",
        "unauthorized transaction",
        "fraud",
        "money stolen",
        "account hacked",
        "charged twice"
    ]

    if any(keyword in issue_lower for keyword in high_priority_keywords):
        priority = "High"
    else:
        priority = result.get("priority", "Medium")

    return {
        "customer_name": customer_name,
        "category": result["category"],
        "priority": priority,
        "suggested_reply": result["suggested_reply"],
        "recommended_solution": result["recommended_solution"]
    }