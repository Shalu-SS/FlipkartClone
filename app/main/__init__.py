from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.main.routes import *

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:omkar@localhost/FlipcartCloneApp"

    app.register_blueprint(user_blueprint, url_prefix="/user")
    app.register_blueprint(category_blueprint, url_prefix="/category")
    app.register_blueprint(product_blueprint, url_prefix="/product")
    app.register_blueprint(cart_blueprint, url_prefix="/cart")

    db.init_app(app)

    return app