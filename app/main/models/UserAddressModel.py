from app.main import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class UserAddressModel(db.Model):
    __tablename__ = "useraddress"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    address = db.Column(db.String(50))