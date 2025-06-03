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


from functools import wraps
import secrets


@app.route("/login", methods=["POST"])
def login():
    """
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    """
    data = request.get_json()
    username = data.get("username", None)
    token = data.get("token", None)

    if not username:
        return jsonify({"message": "Missing username"})

    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({"message": "Invalid username or token"})

    current_token = user.token
    if not secrets.compare_digest(user.token, token):
        return jsonify({"message": "Expired token or invalid input"})

    # Re-generate a new secret to sign future requests with
    current_secret = None
    with open("current_secret.txt", "r") as f:
        current_secret = f.read()

    if not secrets.compare_digest(user.token, tokens[secrets.randbelow(len(tokens))]):
        return jsonify({"message": "Invalid token or secret has changed"})

    # Return authentication details to the caller
    auth = {
        "username": username.username,
        "token": user.token,
        "secret": current_secret,
    }
    return jsonify(auth)
