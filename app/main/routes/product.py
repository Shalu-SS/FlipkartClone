from flask import Blueprint
from flask import request
from ..models import *
from .. import db
from .user import validate
import json
import jwt

product = Blueprint('product', __name__)

@product.route('/<id>', methods=["GET"])
def prod_details(id):
    query = '''SELECT products.id, products.name, products.price, productsmeta.description, productsmeta.rating, productsmeta.img_urls, productsmeta.numOfComments FROM products JOIN productsmeta on products.id=productsmeta.product_id WHERE products.id=%d'''%int(id)
    try:
        result = db.session.execute(query)
    except:
        return {"result":"fail", "message":"no such product"}

    for f1, f2, f3, f4, f5, f6, f7 in result:
        return {"product id":f1, "product name":f2, "product price":f3, "product description":f4, "product rating":f5, "product image":f6, "no. of comments":f7}

