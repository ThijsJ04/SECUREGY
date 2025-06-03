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


from flask import request
import secrets
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password_hash = db.Column(
        db.String(128)
    )  # Generate a secure 128-byte hash for the password

    @staticmethod
    def verify_password(plaintext, hashed):
        return check_password_hash(hashed, plaintext)


def register():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    if User.query.filter_by(username=username).first():  # Check if username exists
        return jsonify({"message": "Username already exists"})

    hashed_password = generate_password_hash(password, method="sha256")
    db.session.add(
        User(username=username, password_hash=hashed_password)
    )  # Store the hashed password in the database
    db.session.commit()
    return jsonify({"message": "User registered successfully"})


def login():
    """
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    """
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not User.query.filter_by(
        username=username
    ).first():  # Check if username exists in the database
        return jsonify({"message": "Username does not exist"})

    if not check_password_hash(
        User.query.get(username).password_hash, token
    ):  # Verify the provided token with the stored hash
        return jsonify({"message": "Invalid token"})

    return jsonify({"message": "Authorized", "token": token})
