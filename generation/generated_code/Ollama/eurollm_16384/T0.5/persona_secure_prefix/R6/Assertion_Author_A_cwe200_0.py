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
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)
logging.basicConfig(level=logging.INFO)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


# Register a user with a unique username and generates a random 16-byte token
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    try:
        db.session.commit()
        return jsonify({"message": "User registered successfully", "token": token})
    except Exception as e:
        logging.error("Error registering user: %s", str(e))
        return jsonify({"message": "Failed to register user", "details": str(e)}), 500


# Login a user with their username and token combination
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    token = request.json.get("token")
    if not username or not token:
        return jsonify({"message": "Invalid request body"}), 400
    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        db.session.delete(
            user
        )  # Remove the user from the session after login to prevent double logins
        return jsonify({"message": "Authorized", "token": token})
    abort(401, description="Unauthorized")
