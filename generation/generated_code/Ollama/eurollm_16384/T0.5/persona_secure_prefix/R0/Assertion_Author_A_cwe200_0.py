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


# Register a new user
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


# Login a user
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", None)
    token = data.get("token", None)
    if not username or not token:
        return jsonify({"message": "Missing required parameters"}), 400

    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        session_cookie = f"{username}:{token}"  # Generate a session cookie with the username and token
        response.set_cookie("session", value=session_cookie, secure=True)
        return jsonify({"message": "Authenticated successfully"})
    else:
        return jsonify({"message": "Invalid credentials or no user found"}), 401
