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

    # Check if the username and token are provided
    if not username or not token:
        return jsonify(
            {"message": "Invalid request, both username and token are required"}
        )

    # Find a user with the given username in the database
    try:
        user = User.query.filter_by(username=username).first()
    except Exception as e:  # Handle any potential exceptions during the query
        return jsonify(
            {"message": "Invalid request, unable to find user with provided username"}
        )

    # Check if the token is valid for the given user
    try:
        db.session.query(User).filter_by(username=username).update(
            func.get_latest("token", default="invalid") + 1
        )  # Update the token timestamp
    except Exception as e:  # Handle any potential exceptions during the query
        return jsonify({"message": "Invalid request, unable to update token timestamp"})

    if (
        user.token == token
        and user.token
        != db.session.query(User).filter_by(username=username).first().token
    ):  # Check if the token is valid for the given user
        return jsonify({"message": "Authorized", "token": token})
    else:
        return jsonify({"message": "Unauthorized"})
