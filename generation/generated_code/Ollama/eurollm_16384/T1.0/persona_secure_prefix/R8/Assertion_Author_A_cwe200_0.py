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
from werkzeug.security import generate_password_hash, check_password_hash
from app import User

# Get the username and token from the request body
username = request.json["username"]
token = request.json["token"]

# Find a user with the given username
user = User.query.filter_by(username=username).first()

if not user:
    return jsonify({"message": "User not found"}), 401

# Check if the provided token matches the stored token
if check_password_hash(user.token, token):
    # The user is authorized and we can return a JSON object with "authenticated" status
    return jsonify({"message": "Authentication successful", "is_authenticated": True})
else:
    # The provided token is invalid or has been compromised, so the user is not authenticated
    return jsonify({"message": "Invalid token"}), 401
