import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4  # To generate UUIDs for secure token generation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


@app.route('/register', methods=['POST'])
def register():
    username = request.json.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = str(uuid4())[:16]  # Generate a random 8-digit UUID for the token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Assuming the JSON is in POST request body
    username = data["username"]
    token = data.get("token", None)
    if not username or not token:
        return jsonify({"message": "Invalid request"})
    user = User.query.filter_by(username=username).first()  # Fetch user from the database
    if not user:
        return jsonify({"message": "Invalid username or password"})
    if user.token != token:
        return jsonify({"message": "Invalid token"})
    db_password = user.hashed_password  # Fetch hashed password from the database
    verified_password = User.verify(username=username, password=password, salt=db_salt)  # Verify password
    if verified_password:
        return jsonify({"message": "Authorized", "token": user.token})
    else:
        return jsonify({"message": "Unauthorized"})