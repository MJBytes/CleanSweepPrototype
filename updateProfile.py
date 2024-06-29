from flask import request, flash, redirect, url_for
from models import db, User

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

