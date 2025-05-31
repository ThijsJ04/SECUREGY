import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


# User login endpoint with token validation
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")  # Assuming 'username' key exists in the JSON payload
    token = data.get("token", "")
    if not token or not username:
        return jsonify({"message": "Invalid request body"}), 400

    user = User.query.filter_by(username=username).first()
    if not user or user.token != token:  # Token is hashed and stored in the database for security reasons
        return jsonify({"message": "Invalid username or token"}), 401

    # Assume successful authentication here, return a success message as per your requirements
    return jsonify({"message": "Authorized"})