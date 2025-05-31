from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(120), nullable=False)
    token = db.Column(db.String(120), nullable=True)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    new_user = User(username=username, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": new_user.id})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Unauthorized"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    user.token = token
    db.session.commit()
    return jsonify({"message": "Authorized", "token": token})