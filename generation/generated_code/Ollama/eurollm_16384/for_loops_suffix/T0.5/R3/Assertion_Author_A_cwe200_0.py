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
    data = request.get_json()
    if not 'username' in data:
        return jsonify({"message": "Missing required field: username"}), 400
    username = data['username']
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not 'username' in data or not 'token' in data:
        return jsonify({"message": "Missing required fields: username and token"}), 400
    username = data['username']
    token = data['token']
    user = User.query.filter_by(username=username).first()
    if not user or user.token != token:
        return jsonify({"message": "Invalid username or token"}), 401
    # Check if the token is still valid (e.g., check expiration time)
    # ...
    return jsonify({"message": "Authenticated successfully", "token": token})