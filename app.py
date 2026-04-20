from flask import Flask
from routes.health import health_bp
from database import db
from routes.expenses import expenses_bp
from routes.categories import categories_bp
from flask_cors import CORS
from config import Config
from flasgger import Swagger

def create_app():
    app = Flask(__name__)

    swagger = Swagger(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

    db.init_app(app)

    app.config.from_object(Config) #loading env variables into app config

    CORS(app, origin=[Config.FRONTEND_URL])
    with app.app_context():

        db.create_all()

    app.register_blueprint(expenses_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(categories_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
