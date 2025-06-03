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
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    """
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not username:  # Check if the "username" key is present in the JSON payload
        return jsonify({"message": "Username missing from request"})

    user = User.query.filter_by(
        username=username
    ).first()  # Query for a user with the given username
    if not user:  # Check if the user exists in the database
        return jsonify({"message": "User does not exist"})

    authenticated_token = (
        user.token
    )  # Get the token associated with the authenticated user

    if (
        token != authenticated_token
    ):  # Compare the provided token against the one stored for the user
        return jsonify(
            {
                "message": "Invalid token",
                "error_description": "Please provide a valid token",
            }
        )

    return jsonify({"message": "Authenticated successfully"})
