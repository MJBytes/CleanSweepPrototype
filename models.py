from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import date

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String(50))
    birth_date = db.Column(db.Date)

    tasks = db.relationship('Task', back_populates='user', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<User {self.email}>'

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))  # No longer required
    is_completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_created = db.Column(db.Date, default=date.today)
    frequency = db.Column(db.String(50))
    area = db.Column(db.String(50))

    user = db.relationship('User', back_populates='tasks')

    def __repr__(self):
        return f'<Task {self.id}>'

