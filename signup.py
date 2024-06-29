from flask import request, flash, redirect, url_for
from flask_login import login_user
from models import db, User

class Signup:
    def post(self):
        email = request.form.get('email')
        password = request.form.get('password')
        if not email or not password:
            flash('Please enter all the fields', 'error')
            return redirect(url_for('main'))

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email address already registered', 'error')
            return redirect(url_for('main'))

        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()

        #Login user
        login_user(user)

        flash('Record was successfully added')
        return redirect(url_for('profile'))
    
    