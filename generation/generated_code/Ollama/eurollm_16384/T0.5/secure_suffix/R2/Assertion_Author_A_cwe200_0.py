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
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///:memory:"  # Use an in-memory database for testing purposes
)
db = SQLAlchemy(app)
jwt = JWTManager(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(
        db.String(120), nullable=False
    )  # Store hashed passwords instead of plain text
    token = db.Column(
        db.String(160), nullable=False
    )  # Store a 32-byte token for each user


# Register route
@app.route("/register", methods=["POST"])
def register():
    username = request.json["username"]
    password_hash = request.json.get(
        "password_hash", ""
    )  # Assume a hashed password is provided in the JSON payload
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, password_hash=password_hash, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


# Login route
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")  # Get the username from the JSON payload
    password_hash = request.json.get(
        "password_hash"
    )  # Get the hashed password from the JSON payload (optional)
    user = User.query.filter_by(
        username=username
    ).first()  # Retrieve the user object by username
    if not user or bcrypt.check_password_hash(user.password_hash, password_hash):
        access_token = create_access_token(
            identity=get_jwt_identity()
        )  # Generate an access token for the authenticated user
        return jsonify({"message": "Authentication successful", "token": access_token})
    return jsonify({"message": "Invalid username or password"}), 401
