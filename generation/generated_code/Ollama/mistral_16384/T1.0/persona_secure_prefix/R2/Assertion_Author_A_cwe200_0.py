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


from flask_login import UserMixin, login_user, current_user, logout_user


class ExtendedUser(User, UserMixin):
    pass


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    user = ExtendedUser.query.filter_by(username=username).first()
    if not user or user.password != password:
        return jsonify({"message": "Unauthorized"})
    login_user(user)
    return jsonify({"message": "Authorized", "token": user.token})
