from flask import Blueprint, request, jsonify
from services.expense_service import create_expense, get_expenses

expenses_bp = Blueprint("expenses", __name__)

@expenses_bp.route("/expenses", methods=["POST"])
def add_expense():
    data = request.json

    idempotency_key = request.headers.get("Idempotency-Key")

    if not data:
        return jsonify({"error": "Invalid request"}), 400

    required_fields = ["amount", "category", "date"]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    try:
        expense = create_expense(data, idempotency_key)
        return jsonify(expense.to_dict()), 201
    except Exception as e:
        return jsonify({"error": "Failed to create expense"}), 500


@expenses_bp.route("/expenses", methods=["GET"])
def list_expenses():
    category = request.args.get("category")
    sort = request.args.get("sort")

    try:
        expenses = get_expenses(category, sort)
        return jsonify([e.to_dict() for e in expenses])
    except Exception:
        return jsonify({"error": "Failed to fetch expenses"}), 500
    