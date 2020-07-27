from app.main import db

class ProductModel(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    price = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
