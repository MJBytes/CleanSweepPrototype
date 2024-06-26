from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users_profile.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for flash messages

db = SQLAlchemy(app)

#import User model after initializing db
from models import User

@app.route('/', methods = ['GET', 'POST'])
def main():
    if request.method == 'POST':
        if not request.form['email'] or not request.form['password']:
            flash('Please enter all the fields' , 'error')
        else:
            User = User(request.form["'email"], request.form['password'])
            db.session.add(User)
            db.session.commit()
            
            flash('Record was successfully added')
            return redirect(url_for('profile.html'))

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
    with app.app_context():
        db.create_all()
    app.run(debug=True)