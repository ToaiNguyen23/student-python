from . import db
from sqlalchemy import *
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),nullable=False)
    address = db.Column(db.String(50),nullable=True)
    numberphone = db.Column(db.String(50),nullable=True)
    gmailaddress = db.Column(db.String(50),nullable=True)
