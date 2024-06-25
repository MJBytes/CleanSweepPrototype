from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

#custom base class for SQLAlchemy models
class Base(DeclarativeBase):
  pass

#create SQL config extension
db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#initialize the app with the extension
db.init_app(app)

@app.route('/')
def main():
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