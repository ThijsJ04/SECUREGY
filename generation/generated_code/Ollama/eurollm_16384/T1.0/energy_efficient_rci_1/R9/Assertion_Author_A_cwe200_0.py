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
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password_hash = db.Column(
        db.String(128), nullable=False
    )  # Larger hash to make brute-force attacks harder
    email = db.Column(db.String(120), nullable=False, index=True)
    token = db.Column(
        db.String(16), nullable=False
    )  # Small token for session management


@app.route("/register", methods=["POST"])
def register():
    if User.query.filter_by(username=request.json.get("username")).first():
        return jsonify({"message": "Username already exists"})
    password = request.json.get("password", "")
    password_hash = generate_password_hash(
        password
    )  # Generate a strong hash of the password
    new_user = User(
        username=request.json.get("username"), password_hash=password_hash, email=""
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(
        {"message": "User registered successfully", "token": secrets.token_hex(16)}
    )


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    if User.query.filter_by(username=username).first():
        user = User.query.filter_by(username=username).first()
        if check_password_hash(
            user.password_hash, password
        ):  # Compare the hash with the provided password
            session_token = secrets.token_hex(16)
            new_session = db.session.add(
                User(username=username, token=session_token)
            )  # Store the token in the database
            db.session.commit()
            return jsonify(
                {"message": "Authentication successful", "token": session_token}
            )
    else:
        return jsonify({"message": "Invalid username or password"})
