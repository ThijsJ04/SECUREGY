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
import time


def login():
    """
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    """

    def authenticate(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            data = args[0].get_json()
            username = data.get("username", "")
            token = data.get("token", "")
            user = User.query.filter_by(username=username, token=token).first()
            if user:
                return f(user, *args[1:], **kwargs)
            else:
                return jsonify({"message": "Unauthorized"})

        return decorated

    @authenticate
    def _inner(user, *args, **kwargs):
        db.session.commit()
        return jsonify({"message": "Authorized"})

    return _inner
