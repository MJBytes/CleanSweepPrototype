from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Task
from datetime import datetime, date
from login import Login
from signup import Signup
from sqlalchemy.exc import SQLAlchemyError
from updateProfile import update_profile
from datetime import date



def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users_profile.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)

#creating and initializing login manager that goes with flask-login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'main'  #This was set to profile in Dev but caused multiple errors

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    return app

app = create_app()

@app.route('/', methods = ['GET', 'POST'])
def main():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'signup':
            signup_instance = Signup()
            return signup_instance.post()
        elif action == 'login':
            login_instance = Login()
            return login_instance.post()
    else:
        return render_template("home.html")

    return redirect(url_for('main'))
    

  
@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():

    user = current_user

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'updateProfile':
            update_instance = update_profile()
            return update_instance.post()

    return render_template('profile.html', user=user)

    
@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def task_view():
    if request.method == 'POST':
        # No need to check session['user_id'], use current_user from Flask-Login
        user_id = current_user.id  # Assuming current_user is a User object with an 'id' attribute
        task_type = request.form['task-type']
        task_date = request.form['task-date']
        task_frequency = request.form['task-frequency']
        task_area = request.form['task-area']

        try:
            task_date = datetime.strptime(task_date, '%Y-%m-%d').date()
        except ValueError:
            flash('Invalid date format for task creation', 'error')
            return redirect(url_for('task_view'))

        description = request.form.get('task-description', '')

        new_task = Task(
            user_id=user_id,
            task_type=task_type,
            description=description,
            date_created=task_date,
            frequency=task_frequency,
            area=task_area
        )

        try:
            db.session.add(new_task)
            db.session.commit()
            flash('Task created successfully!', 'success')
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f'Failed to create task: {str(e)}', 'error')

        return redirect(url_for('task_view'))

    todays_tasks_count = Task.query.filter_by(date_created=date.today()).count()
    completed_tasks_count = Task.query.filter_by(is_completed=True).count()
    uncompleted_tasks_count = Task.query.filter_by(is_completed=False).count()

    return render_template("tasks.html",
                           todays_tasks_count=todays_tasks_count,
                           completed_tasks_count=completed_tasks_count,
                           uncompleted_tasks_count=uncompleted_tasks_count)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/tips')
def tips():
    return render_template("tips.html")

@app.route('/logout')                                   # When user logs out, it redirects to
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main'))



if __name__ == '__main__':
    app.run(debug=True)