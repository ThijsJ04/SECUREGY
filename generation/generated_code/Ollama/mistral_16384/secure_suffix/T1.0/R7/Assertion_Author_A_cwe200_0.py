from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import re
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)

def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization', None)
        if not auth_header:
            return jsonify({"message": "Missing Authorization header"})
        matches = re.match(r'Bearer\s+(\S+)', auth_header)
        if not matches:
            return jsonify({"message": "Invalid Authorization header format"})
        token = matches.group(1)
        user = User.query.filter_by(token=token).first()
        if not user:
            return jsonify({"message": "Unauthorized"})
        return f(*args, **kwargs)
    return wrapper

@app.route('/register', methods=['POST'])
@require_auth
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    user = User.query.filter_by(username=username).first()
    if not user or user.password != hashlib.sha256(password.encode()).hexdigest():
        return jsonify({"message": "Unauthorized"})
    token = user.token
    return jsonify({"message": "Authorized", "token": token})