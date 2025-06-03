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


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


@app.route("/register", methods=["POST"])
def register():
    """
    Register a new user with their provided username and generate a random token for them.
    @return: A JSON object containing the "message" key with a value of "User registered successfully" or an error message if the username already exists.
    """
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
def login():
    """
    Authenticate a user by checking if their provided username and token combination exists in the database.
    @return: A JSON object containing the "message" key with either an "Authorized" or "Unauthorized" value depending on whether the authentication was successful or not.
    """
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    if not username or not token:
        return jsonify({"message": "Invalid input"})
    user = User.query.filter_by(
        username=username
    ).first()  # Check if the user exists in the database
    if not user:
        return jsonify({"message": "Username does not exist"})
    check_token = (
        user.token == token
    )  # Compare the provided token with the one stored for this user
    if not check_token:
        return jsonify({"message": "Invalid token"})
    return jsonify({"message": "Authorized"})
