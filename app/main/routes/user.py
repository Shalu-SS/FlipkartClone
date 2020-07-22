from flask import Blueprint
from flask import request
from ..models.UserModel import UserModel
from .. import db
import json

user = Blueprint('user', __name__)

@user.route('/')
def home():
    return 'user home'

@user.route('/register', methods=["POST"])
def new_user():
    try:
        user = UserModel(email=request.json["email"], password=request.json["password"], mobileNum=request.json["mobileNum"], role=request.json["role"])
        db.session.add(user)
        db.session.commit()
        return 'user added'
    except Exception as e:
        return  str(e)