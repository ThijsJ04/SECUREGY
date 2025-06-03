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

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


# Register route
@app.route("/register", methods=["POST"])
def register():
    if not request.is_json:
        return jsonify({"message": "Invalid request format"}), 400
    data = request.get_json()
    username = data.get("username", "")
    email = data.get("email", "")  # Add email verification for better security
    if not username or not email:
        return jsonify({"message": "Missing username/email field"}), 400
    token = secrets.token_hex(16)
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    try:
        db.session.commit()
        return jsonify({"message": "User registered successfully", "token": token})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Login route
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")  # Remove email for simplicity
    token = data.get("token", None)
    if not username or not token:
        return jsonify({"message": "Missing username/token field"}), 400
    try:
        current_user = User.query.filter_by(username=username).first()
        if not current_user or current_user.token != token:
            return jsonify({"message": "Invalid username/token combination"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return jsonify({"message": "Authorized", "token": token})
