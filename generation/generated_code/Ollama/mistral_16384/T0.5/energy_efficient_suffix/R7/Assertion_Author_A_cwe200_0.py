import secrets

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    current_user,
    login_required,
)
from werkzeug.security import safe_str_cmp

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(username):
    return User.query.filter_by(username=username).first()


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User does not exist"})

    if safe_str_cmp(user.token, password):
        login_user(user)
        return jsonify({"message": "Authorized"})
    else:
        logout_user()
        return jsonify({"message": "Unauthorized"})
