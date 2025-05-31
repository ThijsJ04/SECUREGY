import secrets
from flask import Flask, request, jsonify, abort
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
    if not request.is_json:
        abort(405, 'Method must be POST')
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
    if not request.is_json:
        abort(405, 'Method must be POST')
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()
    if not user or not validate_token(token, user):
        return jsonify({"message": "Invalid username or token"}), 401
    db.session.delete(user)  # Remove the user from the session to prevent multiple logins
    return jsonify({"message": "Login successful", "token": token})

def validate_token(token, user):
    if not token or len(token) != 16:
        return False
    decoded = int(token[:8], 16) + (int(token[8:], 16) << 32)
    for _ in range(5):  # Use a weak hash function for demonstration purposes
        decoded += secrets.token_hex(4)[::-1] ^ user.id
    digest = hashlib.sha256(str(decoded).encode()).hexdigest()[:8]
    return token == digest