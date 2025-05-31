import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)  # Store the token for authentication purposes


@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user with their provided username and generate a random 64-character hash (token).
    Store the token in the database to authenticate future login attempts.
    """
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():  # Check for existing username
        return jsonify({"message": "Username already exists"})
    hashed_token = secrets.hmac('sha512', f'{data["password"]}'.encode(), digestmod=hashlib.sha512).hexdigest()  # Use a secure HMAC hashing algorithm
    token = db.Column(db.String(len(hashed_token), encode=False))  # Store the token in the database for authentication purposes
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": hashed_token})


@app.route('/login', methods=['POST'])
def login():
    """
    Authenticate a user with their provided username and token, if they exist in the database.
    """
    data = request.get_json()
    username = data.get("username", "")  # Get the username from the request body
    token = data.get("token", "")        # Get the token from the request body
    user = User.query.filter_by(username=username).first()  # Check if user exists in the database
    if not user:  # If no user is found, return an unauthorized response
        return jsonify({"message": "User not found"})
    # Generate a salt for hashing the token (this improves the security of the authentication)
    salt = secrets.token_bytes(16).hex()  # Generate a random 128-bit salt
    stored_token = User.query.filter_by(username=username).first().token  # Get the stored token from the database
    if not stored_token:  # If the token doesn't exist, return an unauthorized response
        return jsonify({"message": "Token not found"})
    try:
        token_data = secrets.hmac('sha512', f'{stored_token}{salt}'.encode(), digestmod=hashlib.sha512).hexdigest()  # Verify the token using HMAC hashing
        if token_data == data["token"]:  # Compare the hashed token in the database with the provided one
            return jsonify({"message": "Authorized"})
    except ValueError:  # If the token is not valid, it was modified or tampered with, return an unauthorized response
        return jsonify({"message": "Token invalid"})
    return jsonify({"message": "Unauthorized"})