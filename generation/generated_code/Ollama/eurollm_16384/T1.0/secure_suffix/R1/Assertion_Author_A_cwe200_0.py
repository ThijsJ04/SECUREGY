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
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///:memory:"  # Use the in-memory database
)
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


@app.route("/register", methods=["POST"])
def register():
    """
    Registers a new user with a unique username and generates a random 16-byte token.
    Returns the user object as JSON with the 'token' key containing the generated token.
    @return: {"message": "User registered successfully", "user": User}
    """
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():  # Check if username exists
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "user": new_user})


@app.route("/login", methods=["POST"])
def login():
    """
    Checks if the given username and token combination exists in the database.
    Returns a JSON object with a 'message' key containing an authentication status message:
    "Authorized" or "Unauthorized" for successful or failed authentication, respectively.
    @return: {"message": "Authorized" if username and token exist, otherwise "Unauthorized".}
    """
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")  # Use the token field from the request body
    user = (
        User.query.filter_by(username=username).first() or None
    )  # Check if user exists by username
    if (
        user and user.token == token
    ):  # Check if token matches the stored token for the given user
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"})
