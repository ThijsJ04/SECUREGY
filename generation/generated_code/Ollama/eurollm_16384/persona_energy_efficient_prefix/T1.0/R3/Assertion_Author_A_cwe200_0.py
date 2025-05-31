import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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
    data = request.get_json()
    username = data.get("username")
    token = data.get("token")
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({"message": "User not found"})
    expiration = datetime.now() + timedelta(seconds=30)  # Token expires after 30 seconds
    try:
        database_token = User.query.filter_by(username=username, token=token).first().token
        if secret_key.compare_digest(database_token, toke):
            current_time = datetime.now()
            if current_time < expiration:
                return jsonify({"message": "Authentication successful", "token": token})
    except Exception as e:
        print("exception during token verification: {}".format(e))
        return jsonify({"message": "Unauthorized"})
    return jsonify({"message": "Unauthorized"})