python
import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))  # Use a secure hashing method

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get("username", "")
    password = request.json.get("password", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    password_hash = generate_password_hash(password)
    new_user = User(username=username, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": generate_secret_key(32)})

def generate_secret_key(length):
    """Generate a secret key of the given length."""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(secrets.choice(alphabet) for i in range(length))

@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''