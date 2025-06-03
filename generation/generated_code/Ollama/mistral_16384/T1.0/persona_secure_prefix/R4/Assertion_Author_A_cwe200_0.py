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


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import re

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


def login_required(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        if "token" not in request.json:
            return jsonify({"message": "Missing token for authorization"})
        user = User.query.filter_by(token=request.json["token"]).first()
        if user is None:
            return jsonify({"message": "Unauthorized"})
        return view(*args, **kwargs)

    return wrapper


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = re.sub(
        r"\W+", "", data.get("username", "")
    )  # Remove non-alphanumeric characters from the username
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
@login_required
def login():
    return jsonify({"message": "Authorized"})
