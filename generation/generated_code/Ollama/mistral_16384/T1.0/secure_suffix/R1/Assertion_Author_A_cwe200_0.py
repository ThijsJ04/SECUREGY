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
    current_user,
    login_required,
    login_user,
    logout_user,
)
import bcrypt

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(username):
    user = User.query.filter_by(username=username).first()
    return user


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Username not found"})

    if bcrypt.checkpw(password.encode("utf-8"), user.token.encode("utf-8")):
        login_user(user)
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"})
