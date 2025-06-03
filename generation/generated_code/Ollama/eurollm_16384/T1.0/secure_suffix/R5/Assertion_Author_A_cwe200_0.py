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
    username = request.json[
        "username"
    ]  # Assuming 'username' is present in the JSON object
    token = request.json.get(
        "token", None
    )  # Assumes 'token' is also present in the JSON object
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Username or token does not exist"})
    current_token = user.token  # Get the stored token for this user
    if token != current_token:
        return jsonify({"message": "Invalid token"})
    return jsonify({"message": "Authenticated", "token": token})
