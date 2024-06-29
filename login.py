from flask import request, session, flash, url_for, redirect
from models import db, User
from flask_login import login_user

class Login():
    def post(self):
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            login_user(user) #set our user as logged in
            flash('You logged in successfully')
            return redirect(url_for('profile'))
        else:
            flash('Invalid email or password', 'error')
            return redirect(url_for('main'))


