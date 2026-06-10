from langchain_core.tools import tool

@tool
def handoff(reason: str) -> dict:

    """Signal that this query needs a different specialist. Use when the customer's request is outside your role."""

    return {"needs_handoff": True, "reason": reason}

def check_for_handoff(exec_result: dict) -> dict | None:

    """
    Check agent messages for a handoff tool call.
    Returns handoff dict if found, None otherwise.
    """

    for msg in exec_result["messages"]:
        if hasattr(msg, "tool_calls") and msg.tool_calls:
            for call in msg.tool_calls:
                if call.get("name") == "handoff":
                    args = call.get("args", {})
                    return {
                        "needs_handoff": True,
                        "handoff_reason": args.get("reason", ""),
                        "response": exec_result["messages"][-1].content,
                    }
    return None