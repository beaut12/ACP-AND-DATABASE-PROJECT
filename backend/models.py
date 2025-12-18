from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(200))
    profile_picture = db.Column(db.String(300))

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ref_id = db.Column(db.String(10), unique=True)
    food_type = db.Column(db.String(100))
    food_name = db.Column(db.String(100))
    status = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    expiration = db.Column(db.String(50))
    donor_name = db.Column(db.String(100))
    contact = db.Column(db.String(100))
    delivery = db.Column(db.String(50))
    location = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    reservation_status = db.Column(db.String(20), default="available")
