from models import Expense

def check_existing_request(key):
    if not key:
        return None

    return Expense.query.filter_by(idempotency_key=key).first()
