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
from sqlalchemy import or_
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(256), nullable=False)


@app.route("/register", methods=["POST"])
def register():
    user_data = request.get_json()
    username = user_data.get("username", "")
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    token = data.get("token")

    if not username or not token:
        return jsonify({"message": "Missing required parameters"})

    user = User.query.filter(
        User.username == username
    ).first()  # Check if the user exists in the database

    if not user:
        auth_token = None
    elif user.token != token:
        return jsonify({"message": "Invalid token"})
    else:
        try:
            auth_token = str(
                uuid4()
            )  # Generate a new token for the user and return it as 'auth_token'
            user.token = sha256(
                auth_token
            ).hex()  # Update the user's SHA-256 hashed token in the database
            db.session.commit()
        except Exception as e:
            return jsonify({"message": "Internal server error"})

    return jsonify({"message": "Authenticated successfully", "auth_token": auth_token})
