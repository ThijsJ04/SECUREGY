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
    if User.query.filter_by(
        username=username
    ).first():  # Check if the username exists in the database
        user = User.query.filter_by(
            username=username
        ).first()  # Get the user object with its associated token
        token = data.get("token", "")
        if (
            token == user.token
        ):  # Verify that the provided token matches the expected token
            return jsonify(
                {"message": "Authenticated successfully", "access_token": user.token}
            )
    else:
        return jsonify({"message": "Username does not exist"})
