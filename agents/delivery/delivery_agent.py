from langchain.agents import create_agent
from langchain_core.tools import tool

from agents.tools.safety import is_safe
from agents.tools.handoff import handoff, check_for_handoff
from config.llm_config import get_llm

SYSTEM_PROMPT_TEMPLATE = """
    You are a delivery and shipping specialist at Omnia Retail Ltd, an Irish electronics retailer.

    You help customers with delivery and shipping queries based on Omnia Retail's shipping policy.

    Shipping Policy:
    {policy}

    Your responsibilities:
    1. Answer delivery and shipping questions using the policy
    2. If a customer reports a missing or late order — ask for order ID and check status
    3. If the order needs investigation — signal to check order status
    4. If the order arrived damaged — signal for a refund/replacement
    5. If a customer asks about product availability or stock levels — signal ready_for_action with action_type="check_inventory"

    Important:
    - You do NOT access order systems yourself — signal when backend action is needed
    - If the query is not related to delivery, shipping or inventory - use the handoff tool

    Examples:

    Customer: "How long does delivery take?"
    Response: Explain delivery timeframes from the policy. No action needed.

    Customer: "My order ORD-2024-2045 hasn't arrived"
    Response: Ask for order ID if not given, then signal ready_for_action to check status.

    Customer: "I want to return my laptop"
    Action: handoff(reason="Customer wants a return — not a delivery issue")
"""

# Based on Code for Lab 9 
def _load_policy(documents: list[dict], policy_id: str) -> str:
    policy = next((doc for doc in documents if doc["document_id"] == policy_id), None)
    return policy["content"] if policy else ""

# Based on Code for Lab 9 
@tool
def ready_for_action(order_id: str, issue: str, action_type: str) -> dict:

    """
    Signal that a delivery issue needs backend investigation.

    Args:
        order_id: The order ID in format ORD-YYYY-XXXX
        issue: Description of the delivery issue
        action_type: Either 'check_status', 'report_damaged', or 'report_missing'

    Returns:
        Structured action request for ActionAgent.
    """
    
    return {
        "ready": True,
        "order_id": order_id,
        "issue": issue,
        "action_type": action_type,
    }

# Based on Code for Lab 10
class DeliveryAgent:

    """
    Specialist agent for delivery and shipping queries.
    """

    def __init__(self, documents: list[dict]):
        self.llm = get_llm(temperature=0.2)
        self.policy = _load_policy(documents, "policy_003")
        self.tools = [is_safe, handoff, ready_for_action]

        system_prompt = SYSTEM_PROMPT_TEMPLATE.format(policy=self.policy)

        self.executor = create_agent(
            model=self.llm,
            tools=self.tools,
            system_prompt=system_prompt,
        )

    def process(self, query: str, username: str, history: str = "") -> dict:

        """
        Process a delivery/shipping/inventory query.
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
                            "handoff_reason": f"Delivery action required for order {args.get('order_id')}",
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