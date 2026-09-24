from flask import Flask, render_template, request
from extensions import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portal.db"

db.init_app(app)

from models import Department, User

@app.route("/")
def home():
    return render_template("home.html", name="Eya")

@app.route("/departments")
def departments():
    all_departments = Department.query.all()
    return render_template("departments.html", departments=all_departments)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            return f"Welcome, {user.email}! (role: {user.role})"
        else:
            return "Email or password is incorrect", 401

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)