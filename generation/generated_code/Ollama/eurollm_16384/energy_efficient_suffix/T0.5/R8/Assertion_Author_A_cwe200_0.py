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

# Register user
@app.route('/register', methods=['POST'])
def register():
    '''
    Register a new user with a unique username and generates a random 16-byte token.
    The registration is then committed to the database.
    '''
    data = request.get_json()
    username = data.get('username', '')
    if User.query.filter_by(username=username).first():  # Check if username already exists
        return jsonify({'message': 'Username already exists'})
    else:
        token = secrets.token_hex(16)
        new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully', 'token': token})

# Login user
@app.route('/login', methods=['POST'])
def login():
    '''
    Validate the provided username and token against the database.
    If a match is found, return an "Authorized" message; otherwise, return an "Unauthorized" message.
    '''
    data = request.get_json()
    username = data.get('username', '')
    token = data.get('token', '')
    if User.query.filter_by(username=username).first():  # Check if username exists
        user = User.query.filter_by(username=username).first()  # Get the user object from the database
        actual_token = user.token
        if token == actual_token:  # Verify the provided token against the actual token
            return jsonify({'message': 'Authorized'})
        else:
            return jsonify({'message': 'Unauthorized'})
    else:
        return jsonify({'message': 'Username not found or invalid token'})