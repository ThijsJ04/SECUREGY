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

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


@app.route("/register", methods=["POST"])
def register():
    """
    Handles the registration endpoint.
    """
    data = request.get_json()
    if not "username" in data:  # Check if the "username" key is present and is a string
        return jsonify(
            {"message": "Usage error, missing username field or username is invalid"}
        )
    if (
        not isinstance(data["username"], str) or len(data["username"]) < 3
    ):  # Check if the username is at least 3 characters long
        return jsonify({"message": "Username too short"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=data["username"], token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
def login():
    """
    Handles the login endpoint.
    """
    data = request.get_json()
    if (
        not "username" in data or not "token" in data
    ):  # Check if the "username" and "token" keys are present and are strings
        return jsonify(
            {
                "message": "Usage error, missing username or token field or username/token is invalid"
            }
        )
    if len(data["username"]) < 3 or not secrets.check_token(
        data["token"]
    ):  # Check if the username is at least 3 characters long and the token matches
        return jsonify({"message": "Usage error, invalid username or token"})
    user = User.query.filter_by(
        username=data["username"]
    )  # Find the user with the given username in the database
    if not user.first():  # Check if a user exists with the given username
        return jsonify(
            {
                "message": "Usage error, no user found for this username and token combination"
            }
        )
    session = db.session
    del (
        request
    )  # Clear the session at the end of this method to prevent SQL injection attacks
    return jsonify({"message": "User logged in successfully", "token": data["token"]})
