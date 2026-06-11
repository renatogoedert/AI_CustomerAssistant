# Based on FastMCP documentation — https://gofastmcp.com/getting-started/welcome
# Model Context Protocol specification — https://modelcontextprotocol.io/introduction

"""
Omnia Retail Backend MCP Server.
Exposes order status, refund processing, and inventory checking
as MCP tools that agents can call.

Usage:
    python -m mock_data.mcp_server 

The server runs on http://localhost:8000/mcp by default.
"""

from fastmcp import FastMCP
from mock_data.mock_api import check_order_status, process_refund, check_inventory

mcp = FastMCP(
    name="Omnia Retail Backend",
    instructions="""You have access to Omnia Retail's backend systems.
Use these tools to check order status, process refunds, and check inventory.
Always verify the username matches the order before taking any action."""
)


@mcp.tool
def get_order_status(order_id: str, username: str) -> dict:
    """
    Check the status of a customer order.
    Verifies the order belongs to the logged-in user.

    Args:
        order_id: The order ID in format ORD-YYYY-XXXX
        username: The logged-in customer's username

    Returns:
        Order details including status, items, dates and refund status.
    """
    return check_order_status(order_id, username)


@mcp.tool
def submit_refund(order_id: str, username: str, reason: str) -> dict:
    """
    Process a refund request for a delivered order.
    Only works for delivered orders that haven't already been refunded.

    Args:
        order_id: The order ID in format ORD-YYYY-XXXX
        username: The logged-in customer's username
        reason: The reason for the refund request

    Returns:
        Refund confirmation with refund ID and expected timeline.
    """
    return process_refund(order_id, username, reason)


@mcp.tool
def get_inventory(product_name: str) -> dict:
    """
    Check inventory levels for a product.
    Supports partial name matching.

    Args:
        product_name: Full or partial product name to search for

    Returns:
        Stock levels, price, and availability for matching products.
    """
    return check_inventory(product_name)


if __name__ == "__main__":
    print("Starting Omnia Retail Backend MCP Server...")
    print("Server running at http://localhost:8000/mcp")
    mcp.run(transport="http", host="localhost", port=8000)
