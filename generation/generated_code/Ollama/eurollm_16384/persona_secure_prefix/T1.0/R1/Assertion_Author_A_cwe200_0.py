import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Set the SQLAlchemy database URI to an in-memory SQLite database
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password_hash = db.Column(db.String(128))  # Add a column for the hashed password (e.g., 128 bytes long)


@app.route('/register', methods=['POST'])
def register():
    '''
    Registers a new user with a username and an optional password.
    @param data: The JSON object containing the "username" and "password" keys.
    @return: A JSON response indicating whether registration was successful or not.
    '''
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():  # Check if the username already exists
        return jsonify({"message": "Username already exists"})
    password_hash = generate_password_hash(data.get('password', ''), method='sha256')
    if not data.get('password'):  # If no password is provided, the user must choose a password during registration
        token = secrets.token_hex(16)
        new_user = User(username=data['username'], password_hash=password_hash, token=token)
    else:
        new_user = User(username=data['username'], password_hash=password_hash)  # Update the existing user's password if provided
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route('/login', methods=['POST'])
def login():
    '''
    Checks if the provided username and password combination exists in the database and returns a JSON response with the authentication status.
    @param data: The JSON object containing the "username" and "password" keys.
    @return: A JSON response indicating whether login was successful or not, along with the user's token.
    '''
    data = request.get_json()  # Get the JSON data from the request body
    if User.query.filter_by(username=data['username']).first():  # Check if the username exists in the database
        if check_password_hash(User.query.filter_by(username=data['username']).first().password_hash, data['password']):  # Check the password hash against the provided password
            return jsonify({"message": "Authorized", "token": User.query.filter_by(username=data['username']).first().token})  # Return the token if authentication is successful
        else:
            return jsonify({"message": "Unauthorized"})
    else:
        return jsonify({"message": "Unauthorized"})  # Return unauthorized status for non-existent username