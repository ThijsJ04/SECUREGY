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


from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password_hash = db.Column(db.String(128))
    token = db.Column(
        db.String(16), nullable=False
    )  # Change to 16 characters for consistency with token generation


def register(username):
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    password = request.form["password"]  # Assuming a form submits the password
    hashed_password = generate_password_hash(password)
    new_user = User(
        username=username, password_hash=hashed_password, token=secrets.token_hex(16)
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": new_user.token})
