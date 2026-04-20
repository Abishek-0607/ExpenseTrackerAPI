from database import db
from models import Expense
from utils.idempotency import check_existing_request
from datetime import datetime

def create_expense(data, idempotency_key):
    existing = check_existing_request(idempotency_key)

    if existing:
        return existing  # prevent duplicate

    amount = int(float(data["amount"]) * 100)  # convert to paise

    expense = Expense(
        amount=amount,
        category=data["category"],
        description=data.get("description"),
        date=datetime.fromisoformat(data["date"]).date(),
        idempotency_key=idempotency_key
    )

    db.session.add(expense)
    db.session.commit()

    return expense


def get_expenses(category=None, sort=None):
    query = Expense.query

    if category:
        query = query.filter_by(category=category)

    if sort == "date_desc":
        query = query.order_by(Expense.date.desc())
    else:
        query = query.order_by(Expense.created_at.desc())

    return query.all()
