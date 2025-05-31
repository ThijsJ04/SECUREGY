import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(12), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    if 'username' not in request.json or not request.json['username']:
        return jsonify({"message": "Username is required"})
    data = request.get_json()
    new_user = User(username=data["username"], token=secrets.token_hex(12))
    db.session.add(new_user)
    try:
        db.session.commit()
        return jsonify({"message": "User registered successfully", "token": new_user.token})
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'username' not in data or not data['username'] or 'token' not in data or not data['token']:
        return jsonify({"message": "Username and token are required"})
    try:
        current_user = User.query.filter_by(username=data["username"]).first()
    except Exception as e:
        return jsonify({"message": str(e)})
    if not current_user or current_user.token != data['token']:
        return jsonify({"message": "Invalid username or token"})
    db.session.delete(current_user)
    db.session.commit()
    return jsonify({"message": "Authenticated successfully", "token": current_user.token})