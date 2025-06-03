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
    username = data["username"]
    token = data["token"]

    if User.query.filter_by(
        username=username
    ).first():  # Check if user exists by username
        existing_user = User.query.filter_by(
            username=username
        ).first()  # Get the existing user object
        existing_token = existing_user.token
        if token == existing_token:  # Check if token is valid for the existing user
            return jsonify({"message": "Authorized", "auth_header": {"Token": token}})
    else:
        return jsonify({"message": "Unauthorized"})
