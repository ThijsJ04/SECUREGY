import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():  # Check if username already exists
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route('/login', methods=['POST'])
def login():
    """Verify a user and their associated token."""
    data = request.get_json()
    username = data.get("username")
    token = data.get("token")
    if not username or not token:  # Check if username and/or token is provided
        return jsonify({"message": "Missing credentials"})
    user = User.query.filter_by(username=username).first()  # Find the user by their username
    if not user or not secrets.compare_digest(token, user.token):  # Check if the token matches the stored token
        return jsonify({"message": "Invalid credentials"})
    db.session.delete(user)  # Remove the user after login to release resources
    return jsonify({"message": "Authenticated successfully"})