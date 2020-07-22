from app.main import db

class UserModel(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    mobileNum = db.Column(db.Integer)
    password = db.Column(db.String(50))
    role = db.Column(db.String(50))