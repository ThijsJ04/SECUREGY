import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # SQLite in-memory database
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)

# User registration route
@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})

# User login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')  # Only username and password are required for simplicity
    token = data.get('token')

    user = User.query.filter_by(username=username).first()  # Check if the user exists in the database

    if not user:
        return jsonify({"message": "Unauthorized"})

    if user.token != token:
        return jsonify({"message": "Unauthorized"})

    return jsonify({"message": "Authorized", "token_expires": int(time() * 1000) + 24*60*60*3600  # Token expiration after 24 hours
                   })