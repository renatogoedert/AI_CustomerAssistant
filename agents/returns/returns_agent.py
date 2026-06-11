from langchain.agents import create_agent
from langchain_core.tools import tool

from agents.tools.safety import is_safe
from agents.tools.handoff import handoff, check_for_handoff
from config.llm_config import get_llm

SYSTEM_PROMPT_TEMPLATE = """
    You are a returns and refunds specialist at Omnia Retail Ltd, an Irish electronics retailer.

    You help customers with return and refund requests based on Omnia Retail's returns policy.

    Returns Policy:
    {policy}

    Your responsibilities:
    1. Explain the returns process clearly to the customer
    2. Validate if the customer's request meets the policy requirements
    3. If eligible — confirm the details and signal to process the return
    4. If not eligible — explain why clearly and what alternatives exist

    Important:
    - You do NOT process returns yourself — you validate eligibility and confirm details
    - If the customer has a technical issue (not a return) → use the handoff tool
    - If the customer needs warranty support → use the handoff tool

    Examples:

    Customer: "I want to return my laptop, I changed my mind"
    Response: Check policy for change of mind returns, ask for order ID and purchase date.

    Customer: "My mouse arrived damaged, I want a refund"
    Response: Damaged item — eligible for return. Confirm order ID, then signal ready_for_action.

    Customer: "My laptop screen is flickering"
    Action: handoff(reason="Customer has a technical issue — not a return request")
"""

# Based on Code for Lab 9 
def _load_policy(documents: list[dict], policy_id: str) -> str:

    """Load a specific policy document from the dataset."""

    policy = next((doc for doc in documents if doc["document_id"] == policy_id), None)
    return policy["content"] if policy else ""

# Based on Code for Lab 9 
@tool
def ready_for_action(order_id: str, reason: str, action_type: str) -> dict:

    """
    Signal that return/refund eligibility has been confirmed and action can proceed.

    Args:
        order_id: The order ID in format ORD-YYYY-XXXX
        reason: The reason for the return/refund
        action_type: Either 'refund' or 'return'

    Returns:
        Structured action request for ActionAgent.
    """

    return {
        "ready": True,
        "order_id": order_id,
        "reason": reason,
        "action_type": action_type,
    }

# Based on Code for Lab 10 
class ReturnsAgent:

    """
    Specialist agent for returns and refunds.
    """

    def __init__(self, documents: list[dict], action_agent):
        self.llm = get_llm(temperature=0.2)
        self.action_agent = action_agent
        self.policy = _load_policy(documents, "policy_001")
        self.tools = [is_safe, handoff, ready_for_action]

        system_prompt = SYSTEM_PROMPT_TEMPLATE.format(policy=self.policy)

        self.executor = create_agent(
            model=self.llm,
            tools=self.tools,
            system_prompt=system_prompt,
        )

    def process(self, query: str, username: str, history: str = "") -> dict:
        
        """
        Process a return/refund request.
        Returns {"response", "safe", "needs_handoff", "handoff_reason", "action_taken"}.
        """

        # Safety check
        safety_result = is_safe.invoke(query)
        if not safety_result["safe"]:
            return {
                "safe": False,
                "response": f"I cannot process this request: {safety_result['reason']}",
                "needs_handoff": False,
                "handoff_reason": "",
                "action_taken": None,
            }

        # Run agent
        exec_result = self.executor.invoke({
            "messages": [("human", query)]
        })

        # Check for handoff
        handoff_result = check_for_handoff(exec_result)
        if handoff_result:
            return {**handoff_result, "safe": True}

        # Check for ready_for_action tool call
        for msg in exec_result["messages"]:
            if hasattr(msg, "tool_calls") and msg.tool_calls:
                for call in msg.tool_calls:
                    if call.get("name") == "ready_for_action":
                        args = call.get("args", {})
                        # Pass structured request to ActionAgent
                        action_query = (
                            f"Process a {args.get('action_type', 'refund')} for order "
                            f"{args.get('order_id')} — reason: {args.get('reason')}"
                        )
                        action_result = self.action_agent.process(
                            action_query, username=username
                        )
                        return {
                            "safe": True,
                            "response": action_result["response"],
                            "needs_handoff": False,
                            "handoff_reason": "",
                            "action_taken": args,
                        }

        return {
            "safe": True,
            "response": exec_result["messages"][-1].content,
            "needs_handoff": False,
            "handoff_reason": "",
            "action_taken": None,
        }
