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
    if "username" not in data or "token" not in data:
        return jsonify({"message": "Missing username or token"}), 400
    username = data["username"]
    provided_token = data["token"]

    user = User.query.filter_by(username=username).first()
    if user and user.token == provided_token:
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"}), 401
