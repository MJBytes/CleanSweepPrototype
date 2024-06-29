from flask import request, flash, url_for, redirect
from werkzeug.security import check_password_hash
from models import db, User
from flask_login import login_user

class Login():
    def post(self):
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user) #set our user as logged in
            flash('You logged in successfully')
            return redirect(url_for('profile'))
        else:
            flash('Invalid email or password', 'error')
            return redirect(url_for('main'))


