from flask import Blueprint, jsonify
from database import db
from sqlalchemy import text

health_bp = Blueprint("health", __name__)


@health_bp.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "expense-tracker"
    }), 200


@health_bp.route("/ready", methods=["GET"])
def readiness():
    try:
        db.session.execute(text("SELECT 1"))

        return jsonify({
            "status": "ready",
            "database": "connected"
        }), 200

    except Exception:
        return jsonify({
            "status": "not_ready",
            "database": "disconnected"
        }), 500
