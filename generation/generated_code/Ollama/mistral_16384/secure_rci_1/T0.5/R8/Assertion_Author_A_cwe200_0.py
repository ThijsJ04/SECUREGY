from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import safe_str_cmp, generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(120), nullable=False)
    token = db.Column(db.String(120), nullable=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(password, self.password)

    def authenticate(self, password):
        if self.check_password(password):
            return True
        else:
            return False

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": new_user.token})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User not found"})
    elif user.authenticate(password):
        return jsonify({"message": "Authorized", "token": user.token})
    else:
        return jsonify({"message": "Unauthorized"})