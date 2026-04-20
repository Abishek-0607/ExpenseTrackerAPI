
from models import Expense
from database import db

def retrieve_categories():
    """
    Retrieve unique categories from Expense table.
    """

    results = db.session.query(db.distinct(Expense.category)).all()

    # Flatten tuples → list
    categories = [row[0] for row in results if row[0]]

    return sorted(categories)
