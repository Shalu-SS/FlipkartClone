from app.main import db

class ProductCommentsModel(db.Model):
    __tablename__ = 'productcomments'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comment = db.Column(db.String(256))
    