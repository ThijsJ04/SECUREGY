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
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(
        db.String(120), nullable=False
    )  # Store hashed passwords for security reasons
    hashed_password = db.Column(
        db.String(128), nullable=False, server_default=secrets.token_hex(16)
    )  # Generate a random 16-byte token to store in the database instead of password
    token = db.Column(db.String(120), nullable=False)

    @staticmethod
    def verify_password(plaintext, hashed):
        return check_password_hash(hashed, plaintext)


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(
        username=username, hashed_password=secrets.token_hex(128), token=token
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")  # Get the username from the request body
    password = request.json.get(
        "password", None
    )  # Get the password from the request body (optional)
    if not username or not password:
        return jsonify({"message": "Missing required parameter"}), 400

    plaintext_password = User.verify_password(
        password, User.query.filter_by(username=username).first().hashed_password
    )  # Verify the password using the hashed password stored in the database
    if not plaintext_password:
        return jsonify({"message": "Invalid credentials"})

    token = (
        User.query.filter_by(username=username).first().token
    )  # Get the user's token from the database
    return jsonify({"message": "Authorized", "token": token})
