from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/tasks')
def tasks():
    return render_template("tasks.html")

if __name__ == '__main__':
    app.run(debug=True)
