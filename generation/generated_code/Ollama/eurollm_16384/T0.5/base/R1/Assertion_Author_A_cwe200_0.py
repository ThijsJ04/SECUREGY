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


# Register a user
@app.route("/register", methods=["POST"])
def register():
    # Check if username is not empty and does not already exist in the database
    data = request.get_json()
    if not data or not "username" in data:
        return jsonify({"message": "Missing required field 'username'"})
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=data["username"], token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


# Login a user
@app.route("/login", methods=["POST"])
def login():
    # Check if username and token are provided in the request body
    data = request.get_json()
    if not data or "username" not in data or "token" not in data:
        return jsonify({"message": "Missing required field(s)"})
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.token == data["token"]:
        session_cookie = f"{user.username}:{secrets.token_hex(16)}"  # Generate a random 16-byte token for the session
        response = jsonify(
            {"message": "Authenticated", "session_token": session_cookie}
        )
        response.set_cookie(
            "session_token", session_cookie, max_age=30
        )  # Set a 30-minute expiration time for the session token
    else:
        response = jsonify({"message": "Invalid username or token"})
    return response


# Logout a user
@app.route("/logout", methods=["DELETE"])
def logout():
    session_token = request.cookies.get("session_token")
    if not session_token:
        return jsonify({"message": "No active session found"})
    db.session.delete(
        User.query.filter_by(username=session_token[0]).first()
    )  # Remove the user from the database if necessary
    response = jsonify({"message": "Logged out successfully"})
    return response
