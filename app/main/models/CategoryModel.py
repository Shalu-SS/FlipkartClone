from app.main import db

class CategoryModel(db.Model):
    __tablename__="categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)