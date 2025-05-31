from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from app import User

# Get the username and token from the request body
username = request.json['username']
token = request.json['token']

# Find a user with the given username
user = User.query.filter_by(username=username).first()

if not user:
    return jsonify({'message': 'User not found'}), 401

# Check if the provided token matches the stored token
if check_password_hash(user.token, token):
    # The user is authorized and we can return a JSON object with "authenticated" status
    return jsonify({'message': 'Authentication successful', 'is_authenticated': True})
else:
    # The provided token is invalid or has been compromised, so the user is not authenticated
    return jsonify({'message': 'Invalid token'}), 401