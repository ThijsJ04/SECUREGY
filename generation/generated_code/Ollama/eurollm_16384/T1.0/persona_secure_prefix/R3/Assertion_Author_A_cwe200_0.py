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


def login():
    data = request.get_json()
    username = data["username"]
    token = data["token"]
    if User.query.filter_by(
        username=username
    ).first():  # Check if the username exists in the database
        user = User.query.filter_by(username=username).first()
        if (
            user.token == token
        ):  # Check if the provided token matches the saved one for this username
            return jsonify({"message": "Authorized"})
    return jsonify({"message": "Unauthorized"})
