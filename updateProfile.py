from flask import request, flash, redirect, url_for
from models import db, User
from flask_login import current_user, login_required
from datetime import datetime

class update_profile:
    @login_required
    def post(self):
        email = request.form.get('email')
        name = request.form.get('name')
        dob_day = int(request.form.get('dob-day'))
        dob_month = request.form.get('dob-month')
        dob_year = int(request.form.get('dob-year'))

        if not email or not name or not dob_day or not dob_month or not dob_year:
            flash('Please enter all the fields', 'error')
            return redirect(url_for('profile'))
        
        # validate & combine date of birth
        try:
            birth_date = datetime.strptime(f'{dob_day} {dob_month} {dob_year}', '%d %b %Y').date()
        except ValueError:
            flash('Please enter a valid date of birth', 'error')
            return redirect(url_for('profile'))
        
        user= User.query.filter_by(id=current_user.id).first()

        if user:
            user.email = email
            user.name = name
            user.birth_date = birth_date
            db.session.commit()

            flash('Your information was saved successfully. You can make updates at any time')
            return redirect(url_for('profile'))
        else:
            flash('User not found', 'error')
            return redirect(url_for('profile'))