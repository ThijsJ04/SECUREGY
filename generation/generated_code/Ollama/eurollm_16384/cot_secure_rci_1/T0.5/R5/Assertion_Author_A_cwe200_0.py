import secrets
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)  # Store the token in the database instead of generating it on every request
    hash_token = db.Column(db.String(120))  # Store a hashed version of the token for comparison purposes
    password = db.Column(db.String(80), nullable=False)  # Store the user's password securely using bcrypt

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get("username", "")
    password = request.json.get("password", "")
    if User.query.filter_by(username=username).first():  # Check if a user with the same username already exists
        return jsonify({"message": "Username already exists"})
    hash_token = secrets.token_hex(16)  # Generate a new token for comparison purposes
    new_user = User(username=username, password=generate_password_hash(password), hash_token=hash_token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": hash_token})

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")
    token = request.json.get("token")
    if not username or not token:  # Check if the payload contains both a username and token
        return jsonify({"message": "Invalid payload"})
    user = User.query.filter_by(username=username).first()  # Find the user in the database by username
    if not user or check_password_hash(user.password, generate_password_hash(token)):  # Check if the token matches what's stored for this user
        return jsonify({"message": "Unauthorized"})
    return jsonify({"message": "Authorized", "token": hash_token})