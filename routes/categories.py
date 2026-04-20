from flask import Blueprint, jsonify
from services.categories_service import retrieve_categories
from services.expense_service import create_expense, get_expenses

categories_bp = Blueprint("categories", __name__)

@categories_bp.route("/categories", methods=["GET"])
def get_categories():
    category_list = retrieve_categories()
    return jsonify(category_list), 200
