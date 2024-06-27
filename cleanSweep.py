from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, User

def create_app():
   app = Flask(__name__)
   app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users_profile.db"
   app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
   app.config['SECRET_KEY'] = 'your_secret_key'  # Required for flash messages

#initialize SQLAlchemy instance

   db.init_app(app)

   with app.app_context():
        db.create_all()

   return app

app = create_app()

@app.route('/', methods = ['GET', 'POST'])
def main():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash('Please enter all the fields', 'error')
            return redirect(url_for('main'))

         #check if email already exists
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash('Email address already registered', 'error')
            
        else:
            user = User(email=email, password=password)
            db.session.add(user)
            db.session.commit()
            
            flash('Record was successfully added')
            return redirect(url_for('profile'))

    return render_template("index.html")

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/tasks')
def tasks():
    return render_template("tasks.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/tips')
def tips():
    return render_template("tips.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run(debug=True)