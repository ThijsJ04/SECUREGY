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


from hashlib import sha256
import json


@app.route("/login", methods=["POST"])
def login():
    """
    Get the "username" and "token" from the request body, verify if the user exists, and return an authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    """
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    if not username or not token:
        return jsonify({"message": "Missing required credentials"}), 400

    # Verify the token using the user's password hash (not shown in this example, replace with your actual implementation)
    stored_hash = User.query.filter_by(username=username).first().password_hash
    token_checksum = sha256(token.encode()).hexdigest()
    if stored_hash != token_checksum:
        return jsonify({"message": "Invalid token"}), 401

    # Retrieve the user from the database and return an authentication status message
    user = User.query.filter_by(username=username).first()
    if (
        not user or len(token) != 32
    ):  # For example, consider a token length of 32 bytes for simplicity
        return jsonify({"message": "Unauthorized access attempt"}), 401

    return jsonify({"message": "Authorized", "token": token})
