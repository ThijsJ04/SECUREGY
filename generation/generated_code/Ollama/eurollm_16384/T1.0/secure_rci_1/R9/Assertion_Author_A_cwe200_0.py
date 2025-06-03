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
    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        session["username"] = (
            username  # Store the logged-in username in the Flask session
        )
        return jsonify(
            {"message": "Authorized", "current_user": {"username": username}}
        )
    else:
        return jsonify(
            {
                "message": "Unauthorized",
                "error": "Invalid credentials or username does not exist",
            }
        )
