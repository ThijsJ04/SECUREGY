from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)

@app.route('/register', methods=['POST'])
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

def login_required(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization', None)
        if not auth_header:
            return jsonify({"message": "Missing Authorization header"}), 401
        match = re.match(r'Bearer\s+(\S+)', auth_header)
        token = match.group(1) if match else None
        user = User.query.filter_by(token=token).first()
        if not user:
            return jsonify({"message": "Unauthorized"}), 401
        return view(*args, **kwargs)
    return wrapper

@app.route('/login', methods=['POST'])
@login_required
def login():
    data = request.get_json()
    username = data.get("username", "")
    if not User.query.filter_by(username=username).first():
        return jsonify({"message": "Unauthorized"}), 401
    user.token = secrets.token_hex(16)  # Generate a new token for the user
    db.session.commit()
    return jsonify({"message": "Authorized", "token": user.token})