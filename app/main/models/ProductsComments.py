from app.main import db

class ProductsComments(db.Model):
    __tablename__ = "productscomments"
    id = db.Column(db.Integer, primary_key = True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('userss.id'))
    comment = db.Column(db.String(256))
    