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
        return jsonify({"message": "Invalid request body"}), 400

    user = User.query.filter_by(
        username=username
    ).first()  # Retrieve the user from the database
    if not user or user.token != token:  # Check if the username and token match
        return jsonify({"message": "Invalid credentials"}), 401

    session_token = secrets.token_hex(
        32
    )  # Generate a new session token for security purposes
    user.session_token = session_token
    db.session.commit()

    return jsonify(
        {"message": "Authenticated successfully", "session_token": session_token}
    )
