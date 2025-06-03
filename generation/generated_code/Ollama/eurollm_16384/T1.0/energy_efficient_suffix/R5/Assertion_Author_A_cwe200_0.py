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
    user = User.query.filter_by(
        username=username
    ).first()  # Check if the username exists in the database
    if user is None:
        return jsonify({"message": "Invalid username or password"})
    token_check = User.query.filter_by(token=token).first()
    if token_check is None:  # Check if the token exists in the database
        return jsonify({"message": "Invalid token"})
    user.token = None  # Mark the token as used after successful authentication
    db.session.commit()  # Commit changes to the database
    return jsonify({"message": "Authorized", "token": token_check.token})
