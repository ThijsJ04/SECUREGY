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
import re


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        req_token = kwargs.get("headers").get("X-Token")
        user = User.query.filter_by(token=req_token).first()
        if not user:
            return jsonify({"message": "Unauthorized"})
        return f(*args, **kwargs)

    return decorated


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})

    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/", methods=["GET"])
@login_required
def home():
    return jsonify({"message": "Authorized"})
