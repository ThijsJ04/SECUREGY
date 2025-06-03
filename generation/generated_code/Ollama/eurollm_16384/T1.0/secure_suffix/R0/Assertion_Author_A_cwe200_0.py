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
    data = request.get_json()  # Get the JSON from the request body
    username = data.get("username")  # Get the username from the JSON payload
    token = data["token"]  # Get the token from the JSON payload
    if User.query.filter_by(
        username=username
    ).first():  # Check if a user with this username exists in the database
        user = User.query.filter_by(username=username).first()  # Get that user object
        if (
            user.token == token
        ):  # Check if the provided token matches any existing user tokens for this username
            return jsonify(
                {"message": "Authorized"}
            )  # If they match, return a success message
        else:
            print(
                "WARNING: Token does not match a user's token with the given username"
            )  # Print a warning if they don't match
            return jsonify(
                {"message": "Unauthorized"}
            )  # Return an unauthorized status code
    else:
        print("WARNING: User does not exist in database for given username")
        return jsonify(
            {"message": "Unauthorized"}
        )  # Return a failure message if the user doesn't exist
