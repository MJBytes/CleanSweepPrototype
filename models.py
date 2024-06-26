from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(30))
    birth_date = db.Column(db.Date)
    mobile = db.Column(db.String)