from flask import Blueprint
from flask import request
from ..models import *
from .. import db
from .user import validate
import json
import jwt

cart = Blueprint('cart', __name__)

@cart.route('/', methods=["GET"])
def displayCart():
    res = validate(request.json["auth_token"])
    if not res[0]:
        return json.dumps(res[1])

    user_id = res[1]
    try:
        cart_id = db.session.query(CartModel.id).filter_by(user_id=user_id).all()[0][0]
        return str(cart_id)
    except:
        return {"result":"cart is empty", "message":"please add products"}       
    
    productList = []
    for instance in db.session.query(CartModel).filter_by(cart_id=cart_id).all():
        productList.append({"product_id":instance.product_id, "product_name":instance.product_name, "price":instance.product_price, "quantity":instance.quantity})

    total_price = sum([i["price"] for i in products])

    return {"products":products, "total price":total_price}

@cart.route('/add/<prod_id>', methods=["POST"])
def addToCart(prod_id):
    ''' user is present and product is already added -> increase qty by one
        user is present but not product -> take cart id and add product to cart details table
        user is not present -> add user and product ''' 

    res = validate(request.json["auth_token"])
    if not res[0]:
        return json.dumps(res[1])

    user_id = res[1]
    
    for instance in db.session.query(ProductModel).filter_by(id=prod_id):
        prod_name = instance.name
        prod_price = instance.price

    
    
