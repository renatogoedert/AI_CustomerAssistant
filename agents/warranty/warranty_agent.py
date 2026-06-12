from langchain.agents import create_agent
from langchain_core.tools import tool

from agents.tools.safety import is_safe
from agents.tools.handoff import handoff, check_for_handoff
from config.llm_config import get_llm

SYSTEM_PROMPT_TEMPLATE = """
    You are a warranty specialist at Omnia Retail Ltd, an Irish electronics retailer.

    You help customers with warranty claims based on Omnia Retail's warranty policy.

    Warranty Policy:
    {policy}

    Your responsibilities:
    1. Explain the warranty terms clearly to the customer
    2. Validate if the customer's claim meets the policy requirements
    3. If eligible — confirm the details and signal to process the claim
    4. If not eligible — explain why clearly and what alternatives exist

    Important:
    - You do NOT process warranty claims yourself — you validate eligibility and confirm details
    - If the query is not related to warranty - use the handoff tool
    - Always check purchase date and product condition before confirming eligibility

    Examples:

    Customer: "My laptop stopped working after 8 months, is it under warranty?"
    Response: Check warranty period and conditions, ask for order ID and description of fault.

    Customer: "I dropped my phone and the screen cracked"
    Response: Accidental damage — likely not covered. Explain policy and alternatives.

    Customer: "I want to return my laptop, changed my mind"
    Action: handoff(reason="Customer wants a return — not a warranty claim")
"""

def _load_policy(documents: list[dict], policy_id: str) -> str:
    policy = next((doc for doc in documents if doc["document_id"] == policy_id), None)
    return policy["content"] if policy else ""

@tool
def ready_for_action(order_id: str, reason: str, fault_description: str) -> dict:

    """
    Signal that warranty eligibility has been confirmed and claim can proceed.

    Args:
        order_id: The order ID in format ORD-YYYY-XXXX
        reason: Summary of the warranty claim
        fault_description: Description of the fault or defect

    Returns:
        Structured action request for ActionAgent.
    """

    return {
        "ready": True,
        "order_id": order_id,
        "reason": reason,
        "action_type": "warranty_claim",
        "fault_description": fault_description,
    }


class WarrantyAgent:

    """
    Specialist agent for warranty claims.
    """

    def __init__(self, documents: list[dict]):
        self.llm = get_llm(temperature=0.2)
        self.policy = _load_policy(documents, "policy_002")
        self.tools = [is_safe, handoff, ready_for_action]

        system_prompt = SYSTEM_PROMPT_TEMPLATE.format(policy=self.policy)

        self.executor = create_agent(
            model=self.llm,
            tools=self.tools,
            system_prompt=system_prompt,
        )

    def process(self, query: str, username: str, history: str = "", debug: bool = False) -> dict:

        """
        Process a warranty claim request.
        Returns {"response", "safe", "needs_handoff", "handoff_reason", "action_taken"}.
        """
        
        safety_result = is_safe.invoke(query)
        if not safety_result["safe"]:
            return {
                "safe": False,
                "response": f"I cannot process this request: {safety_result['reason']}",
                "needs_handoff": False,
                "handoff_reason": "",
                "action_taken": None,
            }

        exec_result = self.executor.invoke({
            "messages": [("human", query)]
        })

        # Debug tool calls
        if debug:
            for msg in exec_result["messages"]:
                if hasattr(msg, "tool_calls") and msg.tool_calls:
                    for call in msg.tool_calls:
                        print(f"    [GeneralAgent tool] {call.get('name')} → {call.get('args', {})}")

        # Check for handoff
        handoff_result = check_for_handoff(exec_result)
        if handoff_result:
            return {**handoff_result, "safe": True}

        # Check for ready_for_action
        for msg in exec_result["messages"]:
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                for call in msg.tool_calls:
                    if call.get("name") == "ready_for_action":
                        args = call.get("args", {})
                        return {
                            "safe": True,
                            "response": exec_result["messages"][-1].content,
                            "needs_handoff": True,
                            "handoff_reason": f"Warranty claim confirmed for order {args.get('order_id')}",
                            "route_to": "ActionAgent",
                            "specialist_action": args,
                        }

        return {
            "safe": True,
            "response": exec_result["messages"][-1].content,
            "needs_handoff": False,
            "handoff_reason": "",
            "action_taken": None,
        }
