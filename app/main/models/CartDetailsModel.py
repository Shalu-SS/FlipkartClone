from app.main import db

class CartDetailsModel(db.Model):
    __tablename__ = 'cartdetails'
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    product_name = db.Column(db.String(50))
    product_price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
        