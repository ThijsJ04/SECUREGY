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
    """
    Check if the given "username" and "token" pair exists in the database,
    and return a JSON object with a "message" key containing either "Authorized" or "Unauthorized".
    @return: A JSON object with a "message" key containing the authentication status message.
    """
    data = request.get_json()
    username = data.get(
        "username", ""
    )  # Get the provided username from the request body
    token = data.get(
        "token", ""
    )  # Get the provided token from the request body (default: empty string if not provided)

    # Search for the user with the provided username and token in the database
    user = User.query.filter_by(
        username=username, token=token
    ).first()  # Filter by username and token; if none found, None is returned

    if (
        not user
    ):  # If no matching user is found (meaning invalid credentials or a new account)
        return jsonify({"message": "Unauthorized", "error": "Invalid credentials"}), 401

    # The username and token combination exists in the database, so authenticate the user
    db.session.refresh(
        user
    )  # Refresh the User object to update its attributes (e.g., set the User instance as a bound query parameter)

    return jsonify({"message": "Authorized", "token": user.token})
