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
    """

    return check_order_status(order_id, username)


@mcp.tool
def submit_refund(order_id: str, username: str, reason: str) -> dict:

    """
    Process a refund request for a delivered order.
    """

    return process_refund(order_id, username, reason)


@mcp.tool
def get_inventory(product_name: str) -> dict:

    """
    Check inventory levels for a product.
    """

    return check_inventory(product_name)


if __name__ == "__main__":
    print("Starting Omnia Retail Backend MCP Server...")
    print("Server running at http://localhost:8000/mcp")
    mcp.run(transport="http", host="localhost", port=8000)
