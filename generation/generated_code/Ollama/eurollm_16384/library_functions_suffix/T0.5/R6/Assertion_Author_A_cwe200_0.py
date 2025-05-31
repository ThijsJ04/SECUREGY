import secrets
from flask import Flask, request, jsonify
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
    username = request.json.get("username")
    token = request.json.get("token")
    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        return jsonify({"message": "Authorized", "token": token})
    else:
        return jsonify({"message": "Unauthorized"})

@app.route('/logout', methods=['DELETE'])
def logout():
    current_user = User.query.filter_by(username=request.json.get("username")).first()
    if current_user:
        db.session.delete(current_user)
        db.session.commit()
        return jsonify({"message": "Logged out successfully"})
    else:
        return jsonify({"message": "User not found"}), 401