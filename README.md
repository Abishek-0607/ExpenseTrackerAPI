# ExpenseTrackerAPI
# 💰 Expense Tracker Backend API

A Flask-based REST API for managing expense tracking operations like adding, updating, deleting, and fetching expenses.

---

## 🚀 Features
- Create, update, delete expenses
- Fetch all expenses / filter by date or category
- RESTful API design
- JSON-based responses
- SQLite
- CORS enabled for frontend integration

---

## 🛠️ Tech Stack
- Python 3.10+
- Flask
- Flask-CORS
- SQLAlchemy (or your ORM)
- SQLite

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Abishek-0607/ExpenseTrackerAPI.git
cd expense-tracker-backend

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate 

### 3. Install dependencies
pip install -r requirements.txt

Run Application
flask run

Backend runs at:
http://localhost:5000

📂 Project Structure
src/
│
├── routes/
│   └── categories.py
│   └── expenses.py
│   └── health.py
│
├── services/
│   ├── categories_service.py
│   └── expense_service.py
│
├── utils/
│   └── idempotency.py
│
├── app.py
├── config.py
├── database.py
├── models.py
├── README.md
└──requirements.txt

### Sample Request

POST /expenses
{
"amount": 500,
"category": "Food",
"description": "Lunch",
"date": "2026-04-20"
}

Environment Variables (.env)
FLASK_ENV=development
FRONTEND_URL=http://localhost:5173
DATABASE_URL=sqlite:///expenses.db

CORS
Enabled using Flask-CORS for frontend communication


LIVE API / DEPLOYMENT

Base URL (Deployed Backend):
https://expense-tracker-api-uni6.onrender.com/

API Endpoints

GET /expenses -> Get all expenses
POST /expenses -> Create expense

### Backend Cold Start Behavior
The API is deployed on a free hosting platform.
If the server has been idle, the first request may take ~30–50 seconds to respond due to cold start.
After initialization, responses will be significantly faster.

### TRADE-OFFS AND LIMITATIONS
    Authentication & Authorization: User authentication (JWT, login/signup, role-based access control) was not implemented to keep the system lightweight within the timebox.
    Security Hardening: Advanced security practices (rate limiting, API key validation, request throttling) were not added due to scope limitations.
    CORS Configuration: The backend is configured with open CORS policy to allow requests from all regions, ensuring smooth integration with free deployment platforms.
    Scalability Optimizations: No caching layers (like Redis) or performance optimizations were introduced, as the focus was on building a functional CRUD API.