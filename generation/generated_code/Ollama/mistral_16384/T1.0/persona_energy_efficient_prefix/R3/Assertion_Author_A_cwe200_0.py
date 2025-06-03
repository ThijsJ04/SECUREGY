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


from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user

# Add these imports
from flask import request, jsonify

login_manager = LoginManager()


@login_manager.user_loader
def user_loader(username):
    return User.query.filter_by(username=username).first()


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username, token=token).first()
    if user:
        login_user(user)
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"})
