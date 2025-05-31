import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from cryptography.fernet import Fernet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/example'  # Use a production-grade database
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)  # Use a secure password hashing algorithm

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get("username", "")
    password = request.json.get("password", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    f = Fernet(Fernet.generate_key())  # Use a secure key generation method
    encrypted_password = f.encrypt(password.encode()).decode()
    db.session.add(User(username=username, password_hash=encrypted_password))
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    user = User.query.filter_by(username=username).first()  # Validate user credentials
    if not user or f.decrypt(str(user.password_hash)).decode() != password:
        return jsonify({"message": "Invalid username or password"})
    db.session.add(User(username=username, token="new_token"))  # Generate a new token for authenticated users
    db.session.commit()
    return jsonify({"message": "Authentication successful", "token": user.token})