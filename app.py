from flask import Flask
from database import db
from routes.expenses import expenses_bp

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(expenses_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)