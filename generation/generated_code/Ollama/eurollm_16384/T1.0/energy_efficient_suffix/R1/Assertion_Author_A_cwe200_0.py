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
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()  # Find the user by username
    if not user or not user.verify_token(
        token
    ):  # Check if the token is valid for the given user
        return jsonify({"message": "Unauthorized"})
    db.session.delete(
        user
    )  # Delete the user after login (to prevent multiple sessions)
    return jsonify({"message": "Authorized"})
