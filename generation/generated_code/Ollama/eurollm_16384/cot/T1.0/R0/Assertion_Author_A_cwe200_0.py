from flask import Flask, request, jsonify, session, logging
import secrets
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    password = generate_password_hash(data.get('password', ''), method='sha256')
    new_user = User(username=username, password_hash=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = generate_password_hash(data.get("password"), method="sha256")
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        login_required()
        session['active'] = True
        return jsonify({"message": "Authentication successful"})
    else:
        return jsonify({"message": "Invalid credentials or username not found"})