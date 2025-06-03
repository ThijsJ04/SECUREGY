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


# Token expiration and revocation management
class TokenExpiredException(Exception):
    """Raised when a token has expired."""


def is_token_expired(user, token):
    """Check if the given token has expired."""
    current_time = int(round(time.time() * 1000))  # Convert to milliseconds
    stored_time = user.token[
        -3:
    ]  # Last three characters of the token should be a timestamp in seconds since epoch
    expired = (
        current_time - int(stored_time) >= 60 * 15
    )  # Revoked tokens expire after 15 minutes
    return expired


def revoke_token(user):
    """Revoke the given token by setting it to a random string."""
    db.session.query(User).filter_by(username=user.username).update(
        {"token": secrets.token_hex(120)}
    )
    db.session.commit()
    raise TokenExpiredException("Token has been revoked")


# Token-based authentication
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token for registration
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
def login():
    """
    Get the "username" and "token" from the request body, validate them against the database,
    then verify the token's expiration status using `is_token_expired`. If token is valid but has expired,
    raise a `TokenExpiredException` with an error message. Otherwise, return the user object if found.
    """
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(
        username=username
    ).first()  # Fetch user from the database if found
    if not user:
        return jsonify({"message": "User not found"})

    # Validate token using its last three characters as a timestamp in seconds since epoch
    stored_time = int(
        token[-3:]
    )  # Convert token to an integer for comparison with the stored time
    current_time = int(
        round(time.time() * 1000)
    )  # Convert current time to milliseconds
    if user.token != token or stored_time < current_time:
        return jsonify({"message": "Invalid or expired token"})

    try:
        stored_time = int(
            user.token[-3:]
        )  # Convert stored timestamp to an integer for comparison with the current time
    except ValueError as e:
        raise TokenExpiredException("Token is empty") from e

    if user.username != username or user.token == token:
        db.session.delete(
            user
        )  # Remove old user object if they are different (e.g., account recovery)
    db.session.commit()
    return jsonify({"message": "User authenticated successfully", "user": user})
