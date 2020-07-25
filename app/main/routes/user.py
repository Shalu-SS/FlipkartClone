from flask import Blueprint
from flask import request
from ..models import *
from .. import db
import json
import jwt

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
        try:
            useraddress = UserAddressModel(user_id=request.json["id"], address=request.json["address"])
            db.session.add(useraddress)
            db.session.commit()
        except:
            pass    
        return 'user added'
    except Exception as e:
        return  str(e)

@user.route('/login', methods=["POST"])
def login():
        query = '''SELECT role FROM users where email="%s" and password="%s";''' % (request.json["email"], request.json["password"])
        result = db.session.execute(query)
        data = []
        for row in result:
            data.append(row)
            
        payload = {"email":request.json["email"], "password":request.json["password"], "role":data[0][0]}
        key = "imperium"
        encoded = jwt.encode(payload, key).decode()

        if len(data) == 0:
            return json.dumps({"result":"login Failed", "message":"invalid credentials"})
        
        return json.dumps({"result":"login successful", "auth_token":encoded})
    


@user.route('/add_address', methods=["POST"])
def addAddress():
    try:
        if not len(list(db.session.query(UserModel).filter_by(id = request.json["user_id"]))):
            return "No such user"
        userAddress = UserAddressModel(user_id=request.json["user_id"], address=request.json["address"])
        db.session.add(userAddress)
        db.session.commit()
        return "address added"
    except Exception as e:
        return str(e)    

@user.route("/list", methods=["GET"])
def userlist():

        result = db.session.execute("SELECT users.id, users.email, users.role, users.mobileNum, GROUP_CONCAT(useraddress.address) FROM users join useraddress on users.id = useraddress.user_id group by 1, 2, 3, 4 order by users.id")
        data = []
        for res in list(result):
            data.append({"id":res[0], "email":res[1], "role":res[2], "addresses":res[3]})
        return {"data":data}    

@user.route("/list_addresses", methods=["GET"])
def addresslist():
    