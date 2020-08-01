from flask import Blueprint
from flask import request
from ..models import *
from .. import db
from .user import validate
import json
import jwt

category = Blueprint('category', __name__)

@category.route('/', methods=["GET"])
def home():
    data = []
    for instance in db.session.query(CategoryModel).all():
        data.append({"id":instance.id, "category":instance.name})

    return {"categories":data}

@category.route('/add', methods=["PUT"])
def add():
    res = validate(request.json["auth_token"])
    if not res[0]:
        return json.dumps(res[1])

    if res[2] != "admin":
        return {"access":"denied", "message":"admin access required"}

    category = CategoryModel(name=request.json["name"])
    db.session.add(category)
    db.session.commit()
    return {"result":"success", "message":"category added"}

@category.route('/<id>', methods=["GET"])
def prod_list(id):
    try:
        cat_name = db.session.query(CategoryModel.name).filter_by(id=id).all()[0][0]
    except:
        return {"error":"no such category"}
    data = []

    query = '''SELECT products.id, products.name, productsmeta.img_urls, products.price FROM products JOIN productsmeta ON products.id=productsmeta.product_id WHERE productsmeta.category_id=%d''' %int(id)
    for instance in db.session.execute(query):
        data.append({"product id":instance.id, "product name":instance.name, "img_url":instance.img_urls, "price":instance.price})

    return {"category id":id, "category name":cat_name, "product list":data}

@category.route('/add_products/<cat_id>', methods=["PUT"])
def add_prod(cat_id):
    res = validate(request.json["auth_token"])
    if not res[0]:
        return json.dumps(res[1])
    if res[2] == "user":
        return {"access":"denied", "message":"admin or owner access required"}
    
    try:
        cat_name = db.session.query(CategoryModel.name).filter_by(id=cat_id).all()[0][0]
    except:
        return {"error":"no such category"}

    product = ProductModel(name=request.json["name"], price=request.json["price"], owner_id=res[1])
    db.session.add(product)
    db.session.commit()

    prod_id = db.session.query(ProductModel.id).filter_by(name=request.json["name"]).all()[0][0]
    productmeta = ProductsMetaModel(product_id=prod_id, description=request.json["description"], category_id=cat_id, rating=request.json["rating"], img_urls=request.json["img_urls"], numOfComments=request.json["numOfComments"])
    db.session.add(productmeta)
    db.session.commit()

    return {"result":"success", "message":"product added"}