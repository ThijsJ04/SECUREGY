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


import secrets
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, default=str)
    password = db.Column(db.String(128), nullable=False, default="")


# User model extension for token handling
class ExtendedUser(User):
    extended_user_id = db.Column(
        db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False
    )
    token = db.Column(db.String(120), nullable=True)
    login_attempts = db.Column(db.Integer, default=0, nullable=False)

    @property
    def is_authenticated(self):
        return self.extended_user_id is not None

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value


def register():
    """
    Get the "username" and "password" from the request body and store them in the database. If there is an existing user with this username, a "User Already Exists" error will be returned.
    @return: A JSON object with a "message" key containing either "Authorized" or "Unauthorized" depending on whether the registration was successful or not.
    """
