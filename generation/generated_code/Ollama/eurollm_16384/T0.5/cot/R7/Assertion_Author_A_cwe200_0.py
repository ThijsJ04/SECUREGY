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
    # Retrieve username and token from request body
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    # Check if the provided username exists in the database
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Username does not exist"})

    # Verify the token against the stored token for the given username
    stored_token = user.token
    if token != stored_token:
        return jsonify({"message": "Invalid token"})

    # If the username and token are valid, return a success message
    return jsonify({"message": "Authorized", "token": user.token})
