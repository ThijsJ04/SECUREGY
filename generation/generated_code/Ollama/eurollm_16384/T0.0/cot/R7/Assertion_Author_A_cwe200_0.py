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


from flask import request, jsonify
import hashlib
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_roles

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)
jwt = JWTManager(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password_hash = db.Column(
        db.String(128), nullable=False
    )  # Use a secure hashing algorithm like bcrypt or Argon2


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", "")
    password = request.json.get("password", "")

    if not username:
        return jsonify({"message": "Username is required"}), 400

    try:
        current_user = User.query.filter_by(username=username).first()
        if (
            not current_user
            or current_user.password_hash
            != hashlib.sha256(password.encode()).hexdigest()
        ):
            return jsonify({"message": "Invalid username or password"}), 401
    except Exception as e:
        return jsonify({"message": str(e)}), 500

    access_token = create_access_token(identity=username)
    jwt.add_token(access_token, username)

    return jsonify({"message": "Login successful", "access_token": access_token})
