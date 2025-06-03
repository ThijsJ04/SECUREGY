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


import secrets
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)
jwt = JWTManager(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


# Register user and generate token
@app.route("/register", methods=["POST"])
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


# Login user and generate access token
@app.route("/login", methods=["POST"])
def login():
    username = request.json["username"]
    token = request.json["token"]
    user = User.query.filter_by(username=username).first()
    if not user or user.token != token:
        return jsonify({"message": "Invalid username or token"}), 401
    # Generate access token for the authenticated user
    access_token = create_access_token(identity=username)
    return jsonify(
        {"message": "Authentication successful", "access_token": access_token}
    )


# Protect a route with JWT authentication
@app.route("/protected", methods=["GET"])
@jwt_required
def protected():
    return jsonify({"message": "You are authorized to access this route"})


if __name__ == "__main__":
    app.run(debug=True)
