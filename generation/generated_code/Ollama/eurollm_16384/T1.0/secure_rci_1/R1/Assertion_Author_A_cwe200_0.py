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
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/login", methods=["POST"])
def login():
    """
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    """
    data = request.get_json()
    username = data.get("username", "")
    token = data["token"]
    if not username or not token:
        return jsonify({"message": "Username and token are required"})
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Invalid username or token"})
    if check_password_hash(user.token, token):
        session["token"] = user.token  # Store the current token for later use
        return jsonify({"message": "Authorized", "token": user.token})
    else:
        return jsonify({"message": "Invalid username or token"})
