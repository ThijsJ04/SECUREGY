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


import hashlib
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


# User model
class User(db.Model, bcrypt.BcryptUserMixin):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(60))  # Use a shorter password hash for demo purposes


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", "")
    password = request.json.get("password", "")

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Username does not exist"}), 401

    # Check if the submitted token matches the stored token for the given username
    token = request.json.get("token", None)
    if token and User.query.filter_by(username=username, token=token).first():
        # Verify the password using bcrypt
        stored_password = user.password
        if bcrypt.checkpw(password.encode("utf-8"), stored_password):
            # Return JWT authentication token
            access_token = secrets.token_hex(16)
            db.session.commit()
            return jsonify(
                {"message": "Authenticated successfully", "access_token": access_token}
            )
    else:
        return jsonify({"message": "Invalid token or password"}), 401
