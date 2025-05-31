import secrets
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

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

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    token = request.json['token']
    user = User.query.filter_by(username=username).first()  # Get user from database by username
    if not user or not user.token == token:  # Check if user exists and has the correct token
        return jsonify({"message": "Unauthorized"})
    db.session.delete(user)  # Remove the existing session to prevent double login attempts
    return jsonify({"message": "Authorized", "token": user.token})