import secrets

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import secrets
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(120), nullable=False)


# User registration route
@app.route("/register", methods=["POST"])
def register():
    username = request.json.get("username", "")
    password = request.json.get("password", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    if not isinstance(password, str) or len(password) < 8:
        return jsonify({"message": "Invalid password"}), 401
    password_hash = generate_password_hash(password)
    new_user = User(username=username, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(
        {"message": "User registered successfully", "token": secrets.token_hex(16)}
    )


# User login route
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    user = User.query.filter_by(username=username).first()
    if not user or check_password_hash(user.password_hash, password):
        return jsonify({"message": "Unauthorized"}), 401
    session_token = secrets.token_hex(
        16
    )  # Generate a random 16-byte token for the user's session
    user.session_token = session_token
    db.session.commit()
    return jsonify({"message": "Authorized", "session_token": session_token})
