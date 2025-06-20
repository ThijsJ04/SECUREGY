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
from flask import request, jsonify

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///:memory:"  # sqlite:///:memory: is an in-memory database
)
db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


@app.route("/register", methods=["POST"])
def register():
    """
    Register a new user with a unique username and generates a random 16-byte token for authentication.
    """
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(
        username=username
    ).first():  # Check if the username already exists
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
def login():
    """
    Validate the username and token provided in the request body and check if it exists in the database.
    Return a JSON object with an authentication status message: "Authorized" or "Unauthorized".
    """
    data = request.get_json()
    username = data.get("username", "")  # Extract username from the request body
    token = data.get("token", "")  # Extract token from the request body
    if not (
        username and token
    ):  # Check if both username and token are provided in the request body
        return jsonify({"message": "Invalid request body"})

    user_record = User.query.filter_by(username=username).first()
    if user_record:  # Check if the username exists in the database
        authenticated_token = user_record.token  # Get the token from the user record
        if (
            token == authenticated_token
        ):  # Validate the received token against the stored token
            return jsonify({"message": "Authorized"})
        else:
            return jsonify({"message": "Not Authorized"})
    else:
        return jsonify(
            {"message": "Unauthorized"}
        )  # Return Unauthorized if the username doesn't exist in the database
