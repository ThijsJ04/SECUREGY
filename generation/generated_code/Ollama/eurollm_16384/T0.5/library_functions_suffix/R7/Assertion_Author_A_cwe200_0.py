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


# Register route
@app.route("/register", methods=["POST"])
def register():
    """
    Register a new user with their provided username and generate a random token for authentication.
    """
    data = request.get_json()
    if not "username" in data:
        return jsonify({"message": "Username is required"})
    username = data["username"]
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


# Login route
@app.route("/login", methods=["POST"])
def login():
    """
    Validate the provided username and token for authentication.
    """
    data = request.get_json()
    if not "username" in data or not "token" in data:
        return jsonify({"message": "Username and token are required"})
    username = data["username"]
    token = data["token"]
    user = User.query.filter_by(username=username).first()  # Check if the user exists
    if not user:
        return jsonify({"message": "Username does not exist"})
    if user.token != token:
        return jsonify({"message": "Invalid token"})
    db.session.delete(user)  # Remove the old record to prevent multiple logins
    db.session.commit()
    return jsonify({"message": "Authentication successful"})
