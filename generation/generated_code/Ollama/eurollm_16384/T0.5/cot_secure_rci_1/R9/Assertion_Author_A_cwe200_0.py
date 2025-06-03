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


from flask import jsonify
import bcrypt  # Import a password hashing library (e.g., Flask-Bcrypt)


@app.route("/login", methods=["POST"])
def login():
    """
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    """
    data = request.get_json()
    username = data["username"]  # Extract username from the request body
    token = data["token"]  # Extract token from the request body

    # Hash and verify the password (if provided) using a secure library like Flask-Bcrypt
    if "password" in data:
        password = bcrypt.generate_password_hash(data["password"]).decode(
            "utf-8"
        )  # Generate a salted hash of the password
        user = User.query.filter_by(
            username=username, token=token
        ).first()  # Fetch user from the database
        if user and bcrypt.check_password_hash(
            user.password, password
        ):  # Verify the password using the stored hash
            return jsonify({"message": "Authenticated successfully"})
    else:
        token_valid = (
            secrets.token_hex(16) == token
        )  # Validate the token length and format
        if token_valid:
            user = User.query.filter_by(
                username=username, token=token
            ).first()  # Fetch user from the database
            return jsonify({"message": "Authenticated successfully", "token": token})
    return (
        jsonify({"message": "Unauthorized"}),
        401,
    )  # Return an unauthorized response with a JWT error token (e.g., `Bearer error`)
