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
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


# Register a new user
@app.route("/register", methods=["POST"])
def register():
    username = request.json["username"] if "username" in request.json else ""
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


# Login a user with their username and token
@app.route("/login", methods=["POST"])
def login():
    username = request.json["username"] if "username" in request.json else ""
    token = request.json["token"] if "token" in request.json else None
    if not username or not token:
        return jsonify({"message": "Invalid credentials"})
    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        session["user"] = (
            user  # Store the user object in the Flask-Session for later use
        )
        return jsonify({"message": "Authorized", "user": user})
    else:
        return jsonify({"message": "Unauthorized", "error_code": 401})


# Use the logged in user object to generate a response
@app.route("/protected")
def protected():
    current_user = session["user"] if "user" in session else None
    if current_user:
        return jsonify({"message": "Hello, authenticated user!"})
    else:
        return jsonify({"message": "Not authorized"})
