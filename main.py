from typing import List, Dict, Optional
from datetime import datetime
from mcp.server.fastmcp import FastMCP

# --------------------------------------------------
# In-memory mock data store (acts as a lightweight DB)
# --------------------------------------------------
EMPLOYEE_LEAVES: Dict[str, Dict] = {
    "E001": {
        "balance": 18,
        "history": ["2024-12-25", "2025-01-01"]
    },
    "E002": {
        "balance": 20,
        "history": []
    }
}

# Initialize MCP server
mcp = FastMCP("LeaveManager")


# --------------------------------------------------
# Utility helpers
# --------------------------------------------------
def fetch_employee(employee_id: str) -> Optional[Dict]:
    """
    Retrieve employee leave data.
    Acts as a single access point for employee validation.
    """
    return EMPLOYEE_LEAVES.get(employee_id)


def current_timestamp() -> str:
    """Return current UTC timestamp (ISO format)."""
    return datetime.utcnow().isoformat()


# --------------------------------------------------
# MCP Tools
# --------------------------------------------------
@mcp.tool()
def get_leave_balance(employee_id: str) -> Dict:
    """
    Fetch remaining leave balance for an employee.
    Supported employee IDs: E001, E002
    """
    employee = fetch_employee(employee_id)

    if not employee:
        return {"error": "Employee not found"}

    return {
        "employee_id": employee_id,
        "leave_balance": employee["balance"],
        "checked_at": current_timestamp()
    }


@mcp.tool()
def apply_leave(employee_id: str, leave_dates: List[str]) -> Dict:
    """
    Apply leave for specific dates.
    Example: ["2025-01-15", "2025-01-16"]
    """
    employee = fetch_employee(employee_id)

    if not employee:
        return {"error": "Employee not found"}

    requested_days = len(leave_dates)
    available_balance = employee["balance"]

    if available_balance < requested_days:
        return {
            "status": "rejected",
            "reason": "Insufficient leave balance",
            "available": available_balance,
            "requested": requested_days
        }

    # Update state
    employee["balance"] -= requested_days
    employee["history"].extend(leave_dates)

    return {
        "status": "approved",
        "employee_id": employee_id,
        "days_applied": requested_days,
        "remaining_balance": employee["balance"],
        "processed_at": current_timestamp()
    }


@mcp.tool()
def get_leave_history(employee_id: str) -> Dict:
    """
    Retrieve leave history for an employee.
    """
    employee = fetch_employee(employee_id)

    if not employee:
        return {"error": "Employee not found"}

    return {
        "employee_id": employee_id,
        "leave_history": employee["history"],
        "total_leaves_taken": len(employee["history"])
    }


# --------------------------------------------------
# MCP Resources
# --------------------------------------------------
@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Simple greeting resource."""
    return f"Hello {name}, how can I help you with leave management today?"


# --------------------------------------------------
# Server entrypoint
# --------------------------------------------------
if __name__ == "__main__":
    mcp.run()
