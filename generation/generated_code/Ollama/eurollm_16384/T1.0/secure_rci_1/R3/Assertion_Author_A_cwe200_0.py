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


# Import required modules
import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the application
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///:memory:"  # Create an in-memory database for testing purposes
)
db = SQLAlchemy(app)


# Define the User model with a unique username and a generated token
class User(db.Model):
    username = db.Column(db.String(80), primary_key=True, unique=True)
    token = db.Column(
        db.String(120)
    )  # Generated by the database itself, not by a secret function like secrets.token()


# Implement the register route to store user credentials securely
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():  # Check for duplicate username
        return jsonify({"message": "Username already exists"})
    token = (
        User.generate_token()
    )  # Generate a unique token using the database's token generation logic
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


# Implement the login route to verify user credentials securely
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")  # Fetch the username from the request body
    token = User.verify_token(
        data["token"]
    )  # Verify the provided token against stored tokens using the database's logic
    if not token:
        return jsonify({"message": "Unauthorized"})
    return jsonify(
        {"message": "Authorized", "token": None}
    )  # No need to return the token here since it was verified earlier
