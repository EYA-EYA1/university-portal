from flask import Flask, render_template, request
from extensions import db
from flask_login import LoginManager, login_user, login_required, current_user

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portal.db"
app.config["SECRET_KEY"] = "dev-secret-key-change-later"

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from models import Department, User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return render_template("home.html", name="Eya")

@app.route("/departments")
@login_required
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
            login_user(user)
            return f"Welcome, {user.email}! (role: {user.role}) — You are now logged in."
        else:
            return "Email or password is incorrect", 401

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)