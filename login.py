from flask import request, session, flash, url_for, redirect
from models import db, User

class Login():
    def post(self):
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            session['user_id'] = user.id
            flash('You logged in successfully')
            return redirect(url_for('profile'))
        else:
            flash('Invalid email or password', 'error')
            return redirect(url_for('main'))


class Update_Profile:
    def post(self):
        email = request.form.get('email')
        name = request.form.get('name')
        birth_date = request.form.get('dob-day')
        if not email or not name or not birth_date:
            flash('Please enter all the fields', 'error')
            return redirect(url_for('profile'))
        else:
            user= User(email=email, name=name, birth_date=birth_date)
            db.session.add(user)
            db.session.commit()

            flash('Your information was saved successfully. You can make updates at any time')
            return redirect(url_for('profile'))