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
from bcrypt import hashpw, checkpw

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://localhost/mydatabase"  # Replace with your database URI
)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)  # Store hashed passwords
    token = db.Column(
        db.String(64), nullable=False
    )  # Store a unique token for each user


@app.route("/register", methods=["POST"])
def register():
    username = request.json.get("username", "")
    password = request.json.get("password", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    hashed_password = hashpw(
        password.encode("utf-8"), bcrypt.gensalt()
    )  # Hash the password using bcrypt
    token = secrets.token_hex(16)  # Generate a random 16-byte token for authentication
    new_user = User(username=username, password=hashed_password, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", "")
    password = request.json.get("password", "")
    user = User.query.filter_by(username=username).first()  # Find the user by username
    if not user or checkpw(
        password, hashpw(b"password", user.password)
    ):  # Check if the password matches the hashed password
        return jsonify({"message": "Invalid credentials"})
    token = user.token  # Get the authentication token from the user object
    return jsonify({"message": "Authenticated", "token": token})
