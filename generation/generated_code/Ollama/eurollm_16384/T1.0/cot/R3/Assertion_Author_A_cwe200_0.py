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


import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password_hash = db.Column(db.String(120), nullable=False)  # Hashed password


@app.route("/register", methods=["POST"])
def register():
    if User.query.filter_by(username=request.json.get("username")).first():
        return jsonify({"message": "Username already exists"})
    password = request.json.get(
        "password"
    )  # Use a secure way to get the password from the request body
    if not bcrypt.generate_password_hash(password).startswith("$6"):
        return jsonify({"message": "Invalid password"})
    token = os.urandom(32)  # Generate a cryptographically strong token
    new_user = User(
        username=request.json.get("username"),
        token=token,
        password_hash=bcrypt.generate_password_hash(password),
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()  # Verify the token in plain text is not acceptable, use JWT or other authentication protocols instead
    if not bcrypt.check_password_hash(
        User.query.filter_by(username=data["username"]).first().password_hash,
        data.get("password"),
    ):
        return jsonify({"message": "Invalid username or password"})
    token = data.get(
        "token", None
    )  # Validate the token received from the user against a secure token verification method
    if not token:
        return jsonify({"message": "Token is required for authentication"})
    try:
        auth_header = jwt.decode(
            token, "secret-key"
        )  # Use JWT to verify the user's identity against a secret key stored in Flask or the server configuration
        if not {"username", "token"}.issubset(auth_header):
            return jsonify({"message": "Invalid token"})
    except Exception as e:
        return jsonify(
            {"message": str(e)}
        )  # Handle any errors that occur during token validation
    db.session.expire_all()
    return jsonify({"message": "Authenticated successfully"})
