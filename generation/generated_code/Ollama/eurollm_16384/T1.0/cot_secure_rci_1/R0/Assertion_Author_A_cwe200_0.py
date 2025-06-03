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
    username = data["username"]
    token = data["token"]

    user = User.query.filter_by(
        username=username
    ).first()  # Get the user with the provided username
    if not user:  # If the user does not exist
        return jsonify({"message": "Invalid credentials"})

    if (
        user.token != token
    ):  # Check if the provided token matches the one stored in the database
        return jsonify({"message": "Invalid credentials"})

    db.session.close()  # Close the session to prevent further SQLAlchemy issues
    return jsonify({"message": "Authorized"})
