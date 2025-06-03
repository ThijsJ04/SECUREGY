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


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


@app.route("/register", methods=["POST"])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
def login():
    """Log in a user."""
    username = request.json.get("username")  # Get the username from the JSON payload
    token = request.json.get("token")  # Get the token from the JSON payload
    user = User.query.filter_by(
        username=username
    ).first()  # Find a user with the given username
    if (
        not user or user.token != token
    ):  # Check if the user exists and has the correct token
        return jsonify({"message": "Invalid credentials"}), 401
    session_cookie = (
        f"{username}:{token}"  # Create a session cookie for the authenticated user
    )
    response.set_cookie(
        session_cookie, max_age=3600
    )  # Set the cookie with a one-hour expiration time
    return jsonify({"message": "Authenticated successfully"})
