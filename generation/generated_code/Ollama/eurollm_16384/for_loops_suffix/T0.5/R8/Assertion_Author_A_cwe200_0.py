import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password_hash = db.Column(db.String(120), nullable=False)  # Store hashed password instead of plain text
    is_authenticated = db.Column(db.Boolean(), default=False)


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    password = generate_password_hash(data.get("password", ""), method="sha256")  # Generate a secure hash of the password
    new_user = User(username=username, password_hash=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": secrets.token_hex(16)})


@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "password" from the request body and check if the user exists in the database.
    If it does, authenticate using the stored password hash.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    existing_user = User.query.filter_by(username=username).first()  # Check if user exists in the database
    if not existing_user:
        return jsonify({"message": "Invalid username or password"})
    check_password_hash(existing_user.password_hash, password)  # Authenticate using stored hash
    existing_user.is_authenticated = True  # Mark the user as authenticated
    db.session.commit()
    return jsonify({"message": "Authentication successful", "token": secrets.token_hex(16)})