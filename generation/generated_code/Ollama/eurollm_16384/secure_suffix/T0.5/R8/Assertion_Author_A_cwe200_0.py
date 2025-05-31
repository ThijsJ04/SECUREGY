from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)
jwt = JWTManager(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(120), nullable=False)

# Database initialization
@app.before_first_request
def init_db():
    db.create_all()
    with app.open_resource('users.json') as f:
        for line in f:
            username, password = line.strip().split(',')
            User.query.filter_by(username=username).update({'password': password})
    db.session.commit()

# Register a user
@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    User.create(username=username, password=password)
    jwt.add_token('user', username)  # Add the user to the JWT token store
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": create_access_token(identity=username)})

# Login a user
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return jsonify({"message": "Authentication successful", "token": create_access_token(identity=username)})
    else:
        return jsonify({"message": "Invalid username or password"})