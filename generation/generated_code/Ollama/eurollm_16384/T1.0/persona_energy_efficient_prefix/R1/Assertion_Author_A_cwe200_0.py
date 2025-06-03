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


from flask import request, jsonify
from datetime import datetime, timedelta
import secrets
from app import User  # Import the User model from your Flask application module


def verify_token(user):
    """Verifies a token against a user in the database."""
    current_time = int(round(datetime.utcnow() * 1000))
    if (current_time - user.token_expiration) >= timedelta(minutes=5):
        return True  # Token has not expired yet
    else:
        return False  # Token has expired, return false


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(
        username=username
    ).first()  # Get the user from the database if it exists
    if not user:  # If no matching user found, return an error response
        return jsonify({"message": "User does not exist"})
    if not verify_token(user):  # If token has expired, return an error response
        return jsonify({"message": "Token has expired"})
    db.session.commit()  # Commit the changes to the database
    return jsonify({"message": "Authentication successful", "token": user.token})
