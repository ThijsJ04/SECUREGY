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

    user = User.query.filter_by(
        username=username
    ).first()  # Fetch the user from the database

    if (
        not user or user.token != token
    ):  # Check if the user exists and their token matches
        return jsonify({"message": "Unauthorized"})

    db.session.delete(
        user
    )  # Remove the user's record from the database to prevent unauthorized access
    return jsonify({"message": "Authorized", "token": token})
