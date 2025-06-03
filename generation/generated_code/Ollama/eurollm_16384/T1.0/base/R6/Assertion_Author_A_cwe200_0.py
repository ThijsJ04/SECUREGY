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
    Create a new user with a unique username and generate a random 16-byte token.
    The "username" must be provided in the request body, but it is checked for existence before registration.
    @return: A JSON object with a "message" key containing the registration success message.
    """
    data = request.get_json()
    if (
        not "username" in data
        or not data["username"]
        or User.query.filter_by(username=data["username"]).first()
    ):
        return jsonify({"message": "Invalid or missing username"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=data["username"], token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
def login():
    """
    Get the "username" and "token" from the request body, check if they exist in the database, and return an authentication status message.
    If authentication is successful, a new User session is created in Redis (using Flask-Session).
    @return: A JSON object with a "message" key containing the login success message or an error message if the credentials are invalid or do not match any user.
    """
    data = request.get_json()
    if "username" and "token" in data:
        user = User.query.filter_by(username=data["username"]).first()
        if user is None or user.token != data["token"]:
            return jsonify({"message": "Invalid credentials"})
    else:
        return jsonify({"message": "Missing username and token parameters"})
    session_key = str(
        secrets.token_hex(16)
    )  # Generate a random 16-byte session key for the User session
    db.session.add_all(
        [{"username": user.username, "token": user.token, "session_key": session_key}]
    )  ## Note: this assumes that the data in the json is a dict (i.e., it has a 'username', 'token', and 'session_key' keys)
    db.session.commit()
    return jsonify(
        {"message": "User logged in successfully", "user_id": user.id}
    )  ## Note: the "user_id" will be an integer here, not a string as in User.query.filter_by(username=data['username']).first().id
