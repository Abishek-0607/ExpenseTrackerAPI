from database import db
from datetime import datetime

class Expense(db.Model):
    __tablename__ = "expenses"

    id = db.Column(db.Integer, primary_key=True)

    # store in smallest unit (paise)
    amount = db.Column(db.Integer, nullable=False)

    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255))
    date = db.Column(db.Date, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # for idempotency
    idempotency_key = db.Column(db.String(100), unique=True)

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount / 100,  # convert back to rupees
            "category": self.category,
            "description": self.description,
            "date": self.date.isoformat(),
            "created_at": self.created_at.isoformat(),
        }
