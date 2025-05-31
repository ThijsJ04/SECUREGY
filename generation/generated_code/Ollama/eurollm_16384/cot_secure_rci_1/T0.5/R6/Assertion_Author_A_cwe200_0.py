from flask import Flask, request, jsonify
import hashlib
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/mydatabase'  # Replace with your production database URI
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(60))  # Use a suitable hash length for your chosen library

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    hashed_password = bcrypt.generate_password_hash(data.get("password", ""), salt_rounds=10**7)  # Use a suitable work factor for your chosen library
    token = hashlib.sha256(username.encode() + hashed_password.decode()).hexdigest()  # Hash the username and password together
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})

@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()  # Use the query method to filter by username
    if not user or bcrypt.check_password_hash(hashed_password, data.get("password", "")):  # Verify the password using the library's check_password_hash method
        return jsonify({"message": "Unauthorized"})
    return jsonify({"message": "Authorized"})