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


from flask_login import LoginManager, login_user, current_user, logout_user

# Initialize the Flask-Login manager
login_manager = LoginManager()
login_manager.init_app(app)


def login():
    """
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    If the user is found, log them in and return a JSON object with a "message" key containing the authentication status message: "Authorized".
    If the user is not found or the token is incorrect, return a JSON object with a "message" key containing the authentication status message: "Unauthorized".
    """
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username).first()

    if not user or user.token != token:
        return jsonify({"message": "Unauthorized"})

    login_user(user)  # Log the user in
    return jsonify({"message": "Authorized"})
