from app.main import db

class ProductsMetaModel(db.Model):
    __tablename__="productsmeta"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(products.id))
    description = db.Column(db.String(256))
    category_id = db.Column(db.Integer, db.ForeignKey(categories.id))
    rating = db.Column(db.Integer)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    img_urls = db.Column(db.String(256))
    