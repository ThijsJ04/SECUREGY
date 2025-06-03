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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


# Function to generate a random 32-byte token (more secure than 16 bytes)
def generate_token():
    return secrets.token_bytes(32).hex()


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    # Generate a new token for each user to avoid reusing old tokens
    token = generate_token()
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    try:
        db.session.commit()
    except IntegrityError as e:  # If the user already exists with a different token
        return jsonify({"message": "Username already exists with another token"})
    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(
        username=username
    ).first()  # Fetch user by username (not recommended in production)
    if not user or not validate_token(user, token):
        return jsonify({"message": "Invalid username or token"})
    return jsonify(
        {"message": "Authorized", "username": username}
    )  # Return the logged-in user's username for security reasons
