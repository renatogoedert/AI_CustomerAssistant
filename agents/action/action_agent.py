import asyncio
import json

from fastmcp import Client
from langchain.agents import create_agent
from langchain_core.tools import tool

from agents.tools.safety import is_safe
from agents.tools.handoff import handoff, check_for_handoff
from config.llm_config import get_llm

MCP_SERVER_URL = "http://localhost:8000/mcp"

SYSTEM_PROMPT = """
    You are a customer support action agent for Omnia Retail Ltd, an Irish electronics retailer.

    You can perform the following actions on behalf of customers:
    - Check the status of an order
    - Process a refund for a delivered order
    - Check product inventory and availability
    
    Important rules:
    - Always verify the customer's username matches the order before taking any action
    - Only process refunds for delivered orders
    - If an action fails, explain clearly why and what the customer can do instead
    - If the MCP server is unavailable, inform the customer and suggest contacting support@omniaretail.ie
    - If the customer asks a general information question (return policy, warranty info, delivery times) → use the handoff tool
    - If the customer has a technical issue → use the handoff tool
    
    Examples:
    
    Customer: "What is the status of my order ORD-2024-1891?"
    Action: Call get_order_status with the order ID and username
    
    Customer: "I want a refund for my damaged mouse from order ORD-2024-3012"
    Action: Call submit_refund with order ID, username and reason
    
    Customer: "Is the Samsung NVMe SSD in stock?"
    Action: Call get_inventory with product name
    
    Customer: "What is your return policy?"
    Action: handoff(reason="Customer asking about return policy — information query")
    
    Customer: "My laptop screen is flickering"
    Action: handoff(reason="Customer has a technical issue — screen flickering")
"""

# Based on FastMCP documentation (https://gofastmcp.com/getting-started/welcome)
def _build_mcp_tools(username: str):

    """
    Build LangChain tools that call the MCP server.
    Username is bound at creation time so agents always use the logged-in user.
    """

    # Based on Code for Lab 9
    @tool
    def get_order_status(order_id: str) -> str:

        """
        Check the status of a customer order.
        Args:
            order_id: The order ID in format ORD-YYYY-XXXX
        Returns order details including status, items, and dates.
        """

        async def _call():
            try:
                async with Client(MCP_SERVER_URL) as client:
                    result = await client.call_tool(
                        "get_order_status",
                        {"order_id": order_id, "username": username}
                    )
                    print(f"  [MCP Result] {repr(result)}")                    
                    return str(result)
            except Exception as e:
                return f"Error connecting to backend: {str(e)}. Please contact support@omniaretail.ie"

        return asyncio.run(_call())

    # Based on Code for Lab 9
    @tool
    def submit_refund(order_id: str, reason: str) -> str:

        """
        Process a refund request for a delivered order.
        Args:
            order_id: The order ID in format ORD-YYYY-XXXX
            reason: The reason for the refund request
        Returns refund confirmation with refund ID.
        """

        async def _call():
            try:
                async with Client(MCP_SERVER_URL) as client:
                    result = await client.call_tool(
                        "submit_refund",
                        {"order_id": order_id, "username": username, "reason": reason}
                    )
                    return str(result)
            except Exception as e:
                return f"Error connecting to backend: {str(e)}. Please contact support@omniaretail.ie"

        return asyncio.run(_call())

    # Based on Code for Lab 9
    @tool
    def get_inventory(product_name: str) -> str:

        """
        Check inventory levels for a product.
        Args:
            product_name: Full or partial product name to search for
        Returns stock levels, price and availability.
        """

        async def _call():
            try:
                async with Client(MCP_SERVER_URL) as client:
                    result = await client.call_tool(
                        "get_inventory",
                        {"product_name": product_name}
                    )
                    return str(result)
            except Exception as e:
                print(f"  [MCP Error] {str(e)}") 
                return f"Error connecting to backend: {str(e)}. Please contact support@omniaretail.ie"

        return asyncio.run(_call())

    return [get_order_status, submit_refund, get_inventory]


class ActionAgent:

    """
    Action agent — executes backend operations for customer support.
    Connects to the Omnia Retail MCP server for order, refund and inventory operations.
    Username is bound at init time to ensure correct user context.
    """

    def __init__(self, username: str):
        self.username = username
        self.llm = get_llm(temperature=0)
        self.mcp_tools = _build_mcp_tools(username)
        self.tools = [is_safe] + self.mcp_tools

        self.executor = create_agent(
            model=self.llm,
            tools=self.tools,
            system_prompt=SYSTEM_PROMPT,
        )

    def process(self, query: str,username: str = "", history: str = "") -> dict:

        """
        Process an action request — order status, refund, or inventory check.
        Returns {"safe": bool, "response": str, "actions_taken": list}.
        """

        # Safety check
        safety_result = is_safe.invoke(query)
        if not safety_result["safe"]:
            return {
                "safe": False,
                "response": f"I cannot process this request: {safety_result['reason']}",
                "actions_taken": [],
                "needs_handoff": False,
                "handoff_reason": "",
            }

        # Build query with username context
        active_username = username or self.username
        full_query = f"{query}\n\nNote: The logged-in customer username is '{active_username}'."
        if history:
            full_query = f"Conversation so far:\n{history}\n\nCustomer: {query}\nNote: username is '{active_username}'."

        # Run agent — checks if handoff is needed
        exec_result = self.executor.invoke({
            "messages": [("human", query)]
        })
 
        # Check for handoff
        handoff_result = check_for_handoff(exec_result)
        if handoff_result:
            return {**handoff_result, "safe": True}

        # Build message with history context
        full_query = f"{query}\n\nNote: The logged-in customer username is '{self.username}'."
        if history:
            full_query = f"Conversation so far:\n{history}\n\nCustomer: {query}\nNote: username is '{self.username}'."

        result = self.executor.invoke({
            "messages": [("human", full_query)]
        })

        # Extract tool calls made
        actions_taken = [
            call.get("name", "unknown")
            for msg in exec_result["messages"]
            if hasattr(msg, "tool_calls") and msg.tool_calls
            for call in msg.tool_calls
            if call.get("name") not in ("handoff", "is_safe")
        ]

        response = result["messages"][-1].content

        return {
            "safe": True,
            "response": response,
            "actions_taken": actions_taken,
            "needs_handoff": False,
            "handoff_reason": "",
        }
