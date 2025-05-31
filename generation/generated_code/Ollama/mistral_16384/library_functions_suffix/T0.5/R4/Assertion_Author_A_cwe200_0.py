from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from hashlib import sha256
import hmac

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)

app.config['SECRET_KEY'] = 'your-secret-key'  # Set a secret key for HMAC authentication

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

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username).first()
    if not user or user.token != hmac.new(user.token + app.config['SECRET_KEY'], msg=username.encode('utf-8'), digestmod=sha256).hexdigest():
        return jsonify({"message": "Unauthorized"})
    return jsonify({"message": "Authorized"})