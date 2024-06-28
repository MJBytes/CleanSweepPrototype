from flask import request, session, flash, url_for, redirect
from models import db, User


class Login():
    def post(self):
        email = request.db
        try:
            user = User(email=db['email'])
            user.password = db['password']
            db.session.add(user)
            db.session.commit
            # this line will and the user_id to your session
            session['id'] = user.id

            flash('You logged in Sucessfully')
            return redirect(url_for('profile'))
        
        except:
            user=User(email!=db['email'])

            flash('Email address already registered', 'error')