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


from flask import request

# ... (rest of your code remains the same)


@app.route("/login", methods=["POST"])
def login():
    username = request.json[
        "username"
    ]  # Assuming the 'username' key is present in the JSON payload
    token = request.json["token"]
    user = User.query.filter_by(
        username=username
    ).first()  # Check if the username exists in the database

    if user and user.token == token:
        return jsonify({"message": "Authorized", "token": user.token})
    else:
        return jsonify({"message": "Unauthorized"})
