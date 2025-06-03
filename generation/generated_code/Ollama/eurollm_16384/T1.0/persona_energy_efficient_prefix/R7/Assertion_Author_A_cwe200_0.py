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

    if not username or not token:
        return jsonify({"message": "Invalid input"})

    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        session_token = (
            user.token
        )  # Assign the token to a session variable for subsequent requests
        return jsonify({"message": "Authorized", "session_token": session_token})
    else:
        return jsonify({"message": "Unauthorized"})
