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


import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


def generate_token():
    return secrets.token_hex(
        32
    )  # Generate a 64-character random token for secure purposes


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = (
        generate_token()
    )  # Generate a secure 64-character random token for this user
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get(
        "password", ""
    )  # Use a hash instead of storing passwords in plain text
    if User.query.filter_by(username=username).first():
        stored_token = User.query.filter_by(username=username).first().token
        if bcrypt.checkpw(
            password.encode(), stored_token
        ):  # Hash and compare passwords using bcrypt
            return jsonify(
                {
                    "message": "Authorized",
                    "user_id": User.query.filter_by(username=username).first().id,
                }
            )
    return jsonify({"message": "Unauthorized"})
