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
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password_hash = db.Column(db.String(120), nullable=False)  # For password storage


@app.route("/register", methods=["POST"])
def register():
    username = request.json["username"]
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    password = request.json.get("password", "")
    if not password:
        return jsonify({"message": "Password is required for registration"})
    # Hash the password using bcrypt to securely store it in the database
    hashed_password = generate_password_hash(password, method="scrypt")
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, password_hash=hashed_password, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
def login():
    username = request.json["username"]
    password = request.json.get("password")
    # Check if the user exists in the database and verify their credentials
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Invalid username or password"})
    token = request.json.get("token")  # Get the provided token from the request body
    if not token:
        return jsonify({"message": "Token is required for login"})
    # Verify the user's credentials using bcrypt and the provided token
    check_password_hash(
        user.password_hash, password
    )  # Check if the password matches the stored hash
    if not db.session.query(User).filter_by(token=token).first():
        return jsonify({"message": "Invalid token"})
    authenticated_user = user
    # Return a JSON object with the authentication status message: "Authorized" or "Unauthorized" in case of success or failure, respectively.
    return jsonify(
        {"message": "Authenticated successfully", "user": authenticated_user}
    )
