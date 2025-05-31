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
    '''
    Register a user by creating a new User object with the provided "username" and generating a unique token.
    @return: A JSON object with a "message" key containing either 'User registered successfully' or an error message if the username already exists.
    '''
    data = request.get_json()
    if not 'username' in data or not isinstance(data['username'], str) or len(data['username']) > 80:
        return jsonify({"message": "Invalid username format"}), 400
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=data['username'], token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route('/login', methods=['POST'])
def login():
    '''
    Authenticate a user by verifying the provided "username" and "token" against the User model in the database.
    @return: A JSON object with a "message" key containing either 'Authorized' or 'Unauthorized' depending on whether the provided credentials match an existing user entry in the database.
    '''
    data = request.get_json()
    if not isinstance(data['username'], str) or len(data['username']) > 80:
        return jsonify({"message": "Invalid username format"}), 400
    existing_user = User.query.filter_by(username=data['username']).first()  # Search for a matching user by username
    if not existing_user or existing_user.token != data['token']:
        return jsonify({"message": "Invalid credentials"}), 401
    db.session.refresh(existing_user)  # Refresh the User object in case it was migrated (e.g., on connection to a remote server)
    return jsonify({"message": "Authorized"})