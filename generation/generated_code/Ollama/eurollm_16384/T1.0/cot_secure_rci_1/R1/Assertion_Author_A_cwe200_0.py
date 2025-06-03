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

# Generate a 16-byte (128-bit) random number suitable for managing passwords/secrets
secret_key = secrets.token_bytes(16)
print(secret_key)  # Output: bytes object containing 16 random bytes
