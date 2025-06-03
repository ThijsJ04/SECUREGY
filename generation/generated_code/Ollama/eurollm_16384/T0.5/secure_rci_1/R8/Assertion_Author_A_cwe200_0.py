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


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not username or not token:
        return jsonify(
            {"message": "Invalid input, both username and token are required."}
        ), 400

    user = User.query.filter_by(
        username=username
    ).first()  # Check if the user exists in the database
    if (
        not user or user.token != token
    ):  # Check if the provided token matches the stored one
        return jsonify({"message": "Invalid username or token."}), 401

    session_data = {"username": username, "token": token}
    return jsonify(
        {"message": "Authorized", **session_data}
    )  # Return a JSON object with the user's information
