from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.main.routes import *

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:omkar@localhost/FlipcartCloneApp"

    app.register_blueprint(user_blueprint, url_prefix="/user")

    db.init_app(app)

    return app