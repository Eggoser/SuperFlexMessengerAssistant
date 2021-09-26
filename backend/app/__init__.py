from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pathlib

base_dir = pathlib.Path(__file__).parent

db = SQLAlchemy()


def init_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = ""
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .views import main

    app.register_blueprint(main.main)
    return app
