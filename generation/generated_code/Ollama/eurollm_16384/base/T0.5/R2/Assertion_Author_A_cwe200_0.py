import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Create an in-memory database for testing purposes
db = SQLAlchemy(app)

class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    '''
    Register a new user with a unique username and generate a random 16-byte token for authentication.
    @return: A JSON object with a "message" key containing the registration status message:
    "User registered successfully" or "Username already exists" in case of success or failure, respectively.
    '''
    data = request.get_json()
    username = data.get("username", "")  # Get the username from the request body
    if User.query.filter_by(username=username).first():  # Check if the username already exists in the database
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})

@app.route('/login', methods=['POST'])
def login():
    '''
    Authenticate a user with the provided username and token combination.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()  # Get the username and token from the request body
    username = data.get("username", "")  # Extract the username from the request body
    token = data.get("token", "")  # Extract the token from the request body
    user = User.query.filter_by(username=username).first()  # Find a user with the given username
    if not user or user.token != token:  # Check if the provided token matches the stored token for the given username
        return jsonify({"message": "Unauthorized"})
    db.session.delete(user)  # Remove the authenticated user from the database to prevent multiple logins with the same token
    return jsonify({"message": "Authorized"})