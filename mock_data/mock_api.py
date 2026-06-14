import json
import uuid
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "omnia_backend.json"


def _load_db() -> dict:

    """Load the mock database."""

    return json.loads(DB_PATH.read_text(encoding="utf-8"))


def _save_db(db: dict):

    """Save the mock database."""
    
    DB_PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")

def check_order_status(order_id: str, username: str) -> dict:

    """
    Check the status of an order.
    Returns: {"success": bool, "order": dict | None, "error": str | None}
    """

    try:
        db = _load_db()
        order = db["orders"].get(order_id)

        if not order:
            return {
                "success": False,
                "order": None,
                "error": f"Order {order_id} not found.",
            }

        if order["user"].lower() != username.lower():
            return {
                "success": False,
                "order": None,
                "error": f"Order {order_id} does not belong to this account.",
            }

        return {"success": True, "order": order, "error": None}

    except Exception as e:
        return {"success": False, "order": None, "error": f"API error: {str(e)}"}

def process_refund(order_id: str, username: str, reason: str) -> dict:

    """
    Process a refund for an order.
    Returns: {"success": bool, "refund_id": str | None, "message": str, "error": str | None}
    """

    try:
        db = _load_db()
        order = db["orders"].get(order_id)

        if not order:
            return {
                "success": False,
                "refund_id": None,
                "message": "",
                "error": f"Order {order_id} not found.",
            }

        if order["user"].lower() != username.lower():
            return {
                "success": False,
                "refund_id": None,
                "message": "",
                "error": f"Order {order_id} does not belong to this account.",
            }

        if order["status"] != "delivered":
            return {
                "success": False,
                "refund_id": None,
                "message": "",
                "error": f"Cannot refund order with status '{order['status']}'. Order must be delivered first.",
            }

        if order["refund_status"] == "approved":
            return {
                "success": False,
                "refund_id": None,
                "message": "",
                "error": f"Order {order_id} has already been refunded.",
            }

        # Process refund
        refund_id = f"REF-{uuid.uuid4().hex[:8].upper()}"
        refund_record = {
            "refund_id": refund_id,
            "order_id": order_id,
            "username": username,
            "reason": reason,
            "amount": order["total"],
            "status": "approved",
            "date": datetime.now().isoformat(),
        }

        # Update order and save
        db["orders"][order_id]["refund_status"] = "approved"
        db["refunds"][refund_id] = refund_record
        _save_db(db)

        return {
            "success": True,
            "refund_id": refund_id,
            "message": f"Refund of €{order['total']} approved. Refund ID: {refund_id}. "
                       f"Amount will be returned to your original payment method within 5-7 business days.",
            "error": None,
        }

    except Exception as e:
        return {"success": False, "refund_id": None, "message": "", "error": f"API error: {str(e)}"}


def check_inventory(product_name: str) -> dict:

    """
    Check inventory levels for a product.
    Returns: {"success": bool, "results": list, "error": str | None}
    """
    try:
        db = _load_db()
        inventory = db["inventory"]

        # Exact match 
        if product_name in inventory:
            item = inventory[product_name]
            return {
                "success": True,
                "results": [{
                    "product": product_name,
                    "stock": item["stock"],
                    "price": item["price"],
                    "category": item["category"],
                    "available": item["stock"] > 0,
                }],
                "error": None,
            }

        # Partial match
        matches = [
            {
                "product": name,
                "stock": item["stock"],
                "price": item["price"],
                "category": item["category"],
                "available": item["stock"] > 0,
            }
            for name, item in inventory.items()
            if product_name.lower() in name.lower()
        ]

        if matches:
            return {"success": True, "results": matches, "error": None}

        return {
            "success": False,
            "results": [],
            "error": f"No products found matching '{product_name}'.",
        }

    except Exception as e:
        return {"success": False, "results": [], "error": f"API error: {str(e)}"}

