from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Task
from datetime import datetime, date
from login import Login
from signup import Signup
from sqlalchemy.exc import SQLAlchemyError


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users_profile.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)

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



@app.route('/profile')
def profile():
    if 'user_id' not in session:
        flash('Please log in to access your profile', 'error')
        return redirect(url_for('main'))

    user_id = session['user_id']
    user = User.query.get(user_id)

    if not user:
        flash('Invalid email or password', 'error')
        return redirect(url_for('main'))

    #pass user data to the remplate
    return render_template('profile.html', user=user)


@app.route('/tasks', methods=['GET', 'POST'], endpoint='tasks')
def task_view():
    if request.method == 'POST':
        if 'user_id' not in session:
            flash('Please log in to create tasks', 'error')
            return redirect(url_for('main'))

        user_id = session['user_id']
        task_type = request.form['task-type']
        task_date = request.form['task-date']
        task_frequency = request.form['task-frequency']
        task_area = request.form['task-area']

        # Convert task_date to a Python date object if necessary
        try:
            task_date = datetime.strptime(task_date, '%Y-%m-%d').date()
        except ValueError:
            flash('Invalid date format for task creation', 'error')
            return redirect(url_for('tasks'))

        # This is to ensure description is provided or set a default value
        # To keep it simple, setting it to an empty string if not provided
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

        return redirect(url_for('tasks'))

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
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('main'))



if __name__ == '__main__':
    app.run(debug=True)