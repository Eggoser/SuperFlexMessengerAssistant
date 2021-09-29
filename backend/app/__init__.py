from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from flask_cors import CORS
import pathlib
import os
from dotenv import load_dotenv

base_dir = pathlib.Path(__file__).parent

load_dotenv(base_dir.parent / ".env")

# db = SQLAlchemy()
cors = CORS()
secret_key = os.environ.get("SECRET_KEY")
mongo = MongoClient(os.environ.get("MONGO_URI"))


def init_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{base_dir.parent}/test.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    # db.init_app(app)
    cors.init_app(app, supports_credentials=True)

    from .views import main

    app.register_blueprint(main.main)

    # with app.app_context():
    #     db.create_all()

    return app
