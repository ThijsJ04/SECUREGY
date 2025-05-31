import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from bcrypt import hashpw, checkpw

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)  # 128-byte salt and hash for demonstration purposes

@app.route('/register', methods=['POST'])
def register():
    if not User.query.filter_by(username=request.json['username']).first():
        password = request.json['password']  # Use the provided password for demonstration purposes
        hashed_password = hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(username=request.json['username'], password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully", "token": secrets.token_hex(16)})  # Generate a random 16-byte token
    else:
        return jsonify({"message": "Username already exists"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "Unauthorized"})  # Authentication failed if user does not exist in database
    elif checkpw(data['password'].encode('utf-8'), User.query.filter_by(username=data['username']).first().password_hash):
        return jsonify({"message": "Authorized", "token": secrets.token_hex(16)})  # Generate a random 16-byte token upon successful login
    else:
        return jsonify({"message": "Unauthorized"})  # Authentication failed if password is incorrect or has not been updated since last login attempt