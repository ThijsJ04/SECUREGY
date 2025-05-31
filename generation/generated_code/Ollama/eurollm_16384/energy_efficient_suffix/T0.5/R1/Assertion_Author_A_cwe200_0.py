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

# Register a user
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

# Login a user
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")
    token = request.json.get("token")
    if not username or not token:
        return jsonify({"message": "Missing required parameters"})
    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        session['user'] = user  # Store the user in a Flask-Session object for future requests
        return jsonify({"message": "Authenticated successfully", "token": token})
    else:
        return jsonify({"message": "Invalid username or token"})