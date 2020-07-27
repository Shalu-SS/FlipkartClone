from flask import Blueprint
from flask import request
from ..models import *
from .. import db
import json
import jwt

user = Blueprint('user', __name__)

def validate(auth_token):
    try:
        key = "secret"
        decoded = jwt.decode(auth_token, key)
        return True, decoded["id"], decoded["role"] 
    except:
        return False, {"result":"authentication failed", "message":"invalid token"}    

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
            # If address is given during registeration add it otherwise pass
            useraddress = UserAddressModel(user_id=request.json["id"], address=request.json["address"])
            db.session.add(useraddress)
            db.session.commit()
        except:
            pass    
        return {"result":"success", "message":'user added'}
    except Exception as e:
        return  str(e)

@user.route('/login', methods=["POST"])
def login():
        query = '''SELECT id, role FROM users where email="%s" and password="%s";''' % (request.json["email"], request.json["password"])
        result = db.session.execute(query)
        data = []
        for row in result:
            data.append(row)
            
        payload = {"email":request.json["email"], "password":request.json["password"], "role":data[0][1], "id":data[0][0]}
        key = "secret"
        encoded = jwt.encode(payload, key).decode()

        if len(data) == 0:
            return json.dumps({"result":"login Failed", "message":"invalid credentials"})
        
        return json.dumps({"result":"login successful", "auth_token":encoded})
    
@user.route('/add_address', methods=["POST"])
def addAddress():
    res = validate(request.json["auth_token"])
    if not res[0]:
        return json.dumps(res[1])

    userAddress = UserAddressModel(user_id=res[1], address=request.json["address"])
    db.session.add(userAddress)
    db.session.commit()
    return {"result":"success", "message":"address added"}

@user.route("/list", methods=["GET"])
def userlist():
    res = validate(request.json["auth_token"])

    if not res[0]:
        return json.dumps(res[1])

    if res[2] != "admin":
        return {"access":"denied", "message":"admin access required"}    
        
    result = db.session.execute("SELECT users.id, users.email, users.role, users.mobileNum, GROUP_CONCAT(useraddress.address) FROM users left join useraddress on users.id = useraddress.user_id group by 1, 2, 3, 4 order by users.id")
    data = []
    for res in list(result):
        data.append({"id":res[0], "email":res[1], "role":res[2], "mobileNum":res[3], "address":res[4]})
    return {"data":data}    

@user.route("/list_address", methods=["GET"])
def addresslist():
    res = validate(request.json["auth_token"])

    if not res[0]:
        return json.dumps(res[1])

    data = []
    for instance in db.session.query(UserAddressModel.address).filter_by(user_id=res[1]).all():
        data.append(instance.address)

    return {"user_id":res[1], "addresses":data}        

@user.route("/delete_address", methods=["DELETE"])
def deleteAddress():
    res = validate(request.json["auth_token"])

    if not res[0]:
        return json.dumps(res[1])

    query = '''DELETE FROM useraddress WHERE id=%d;''' % request.json["address_id"] 
    db.session.execute(query)
    db.session.commit()
    return {"result":"success", "message":"address deleted"}
           