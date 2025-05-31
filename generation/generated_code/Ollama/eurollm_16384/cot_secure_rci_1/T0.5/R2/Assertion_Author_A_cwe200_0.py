from flask import Flask, request, jsonify
import secrets
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)
jwt = JWTManager(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)  # Use a secure hash function like bcrypt

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    if not User.query.filter_by(username=username).first():
        return jsonify({"message": "Invalid username or password"})
    elif not check_password_hash(User.query.get(1).password_hash, generate_password_hash(password)):
        return jsonify({"message": "Invalid password"})
    access_token = create_access_token(identity=username)  # Generate a JWT with the user's identity
    jwt.publish_permissions(username, ['login'])  # Publish permissions for the logged-in user
    return jsonify({"message": "User logged in successfully", "access_token": access_token})