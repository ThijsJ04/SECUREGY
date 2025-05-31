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

# Register route
@app.route('/register', methods=['POST'])
def register():
    if not request.is_json:
        return jsonify({"message": "Invalid request format"}), 400
    data = request.get_json()
    username = data.get("username", "")
    if not username or len(username) > 80:
        return jsonify({"message": "Username must be between 1 and 80 characters long"}), 400
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})

# Login route
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"message": "Invalid request format"}), 400
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    if not username or len(username) > 80:
        return jsonify({"message": "Username must be between 1 and 80 characters long"}), 400
    user = User.query.filter_by(username=username).first()
    if user is None or not user.verify_token(token):
        return jsonify({"message": "Invalid username or token"}), 401
    db.session.delete(user)  # Remove the user from the session after login to avoid duplicate entries
    return jsonify({"message": "Authenticated", "token": token})