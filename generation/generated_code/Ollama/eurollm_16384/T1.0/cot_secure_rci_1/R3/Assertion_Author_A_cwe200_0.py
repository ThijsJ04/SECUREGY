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
import os

# Generate a random 16-byte (128 bits) token
token = secrets.token_bytes(16)

# Convert the bytes to hexadecimal format
token = "".join(
    "%02x" % ord(c) for c in token
).decode()  # Using ord() and join() functions
