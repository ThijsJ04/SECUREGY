from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)

    def set_password(self, password):
        self.token = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest() == self.token

# Helper function to protect routes
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or User.query.filter_by(token=token).first() is None:
            return jsonify({"message": "Unauthorized"}), 401
        user = User.query.filter_by(token=token).first()
        request.user = user
        return f(*args, **kwargs)
    return decorated

@app.route('/register', methods=['POST'])
@login_required
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    user = User(username=username)
    db.session.add(user)
    user.set_password(secrets.token_hex(16))
    db.session.commit()
    user.token = user.token[:12]  # Truncate token to 12 characters for security
    return jsonify({"message": "User registered successfully", "token": user.token})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"message": "Unauthorized"}), 401
    user.token = user.token[:12]  # Truncate token to 12 characters for security
    request.user = user
    return jsonify({"message": "Authorized"})