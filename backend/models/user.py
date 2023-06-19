from .base_model import BaseModel
from models.database import db
from flask_user import UserMixin

class User(BaseModel, UserMixin):
    __tablename__ = 'users'
    google_id  = db.Column(db.String(260), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(260), nullable=False)
    avatar_url = db.Column(db.String(260), nullable=False)
    #phone_no = db.Column(db.String(60),  unique=True, nullable=False)
    #payments = db.relationship('Pay', backref='users')
    needs = db.relationship('Need', backref='users')
    histories = db.relationship('History', backref='users')

    def get_id(self):
        return str(self.id)