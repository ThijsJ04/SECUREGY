from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


@app.route('/register', methods=['POST'])
def register():
    # ... (same as your original code)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    if not username or not token:
        return jsonify({"message": "Invalid request body"})
    user = User.query.filter_by(username=username).first()  # Check if the user exists
    if not user or user.token != token:
        return jsonify({"message": "Unauthorized", "error": "Incorrect username or token"})
    db.session.delete(user)  # Remove the user from the session to prevent multiple logins
    return jsonify({"message": "Authorized"})