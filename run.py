from flask import Flask, render_template
from extensions import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portal.db"

db.init_app(app)

from models import Department

@app.route("/")
def home():
    return render_template("home.html", name="Eya")

@app.route("/departments")
def departments():
    all_departments = Department.query.all()
    return render_template("departments.html", departments=all_departments)

if __name__ == "__main__":
    app.run(debug=True)