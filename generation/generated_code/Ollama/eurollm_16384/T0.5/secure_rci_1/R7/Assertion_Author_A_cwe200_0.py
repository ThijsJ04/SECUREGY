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
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_roles,
    get_current_identity,
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)
jwt = JWTManager(app)


# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # Role can be 'admin', 'user' etc.


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"message": "Missing username parameter"}), 400
    username = data["username"]
    if User.query.filter_by(username=username).first():
        return jsonify({"message": f"Username '{username}' already exists"})
    password = secrets.token_urlsafe(120)  # Generate a random 120-byte password
    new_user = User(username=username, password=password, role="user")
    db.session.add(new_user)
    db.session.commit()
    return jsonify(
        {
            "message": "User registered successfully",
            "token": create_access_token(identity=username),
        }
    )


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"message": "Missing username parameter"}), 400
    username = data["username"]
    if User.query.filter_by(username=username).first():
        password = (
            request.form.get("password") or None
        )  # Use the password from the request form if provided, otherwise use a random one
        user = User.query.filter_by(username=username).first()
        if not user or (password and user.password != secrets.token_bytes(120)):
            return jsonify({"message": "Invalid username or password"})
        access_token = create_access_token(
            identity=username, role=user.role
        )  # Generate a JWT for the user
        return jsonify({"message": "Authenticated successfully", "token": access_token})
