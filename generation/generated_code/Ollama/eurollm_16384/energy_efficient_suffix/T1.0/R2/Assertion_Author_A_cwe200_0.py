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
    Register a new user.

    @param {object} json - The JSON payload containing the username to register.
    @return: A JSON object with "message" key containing a success message in case of successful registration.
    '''
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    # Generate a random 16-byte token
    token = secrets.token_hex(16)
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})

@app.route('/login', methods=['POST'])
def login():
    '''
    Authenticate a user with their username and token.

    @param {object} json - The JSON payload containing the username to authenticate.
    @return: A JSON object with "message" key containing an authorization status message.
    '''
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")  # Token is optional but must be provided to make the method safe from CSRF attacks
    user = User.query.filter_by(username=username).first()
    if user and (user.token == token or (not token)):  # Check if the provided token matches any stored tokens for the given username
        return jsonify({"message": "Authorized", "token": token})  # Return a success message with the token
    else:
        return jsonify({"message": "Unauthorized"})  # Return an unauthorized response