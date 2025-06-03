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


def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        # Check password or verify the token using a secret (not shown)
        authenticated_user = user
        return jsonify(
            {"message": "Authorized", "authenticated_user": authenticated_user}
        )
    else:
        return jsonify({"message": "Unauthorized"})
