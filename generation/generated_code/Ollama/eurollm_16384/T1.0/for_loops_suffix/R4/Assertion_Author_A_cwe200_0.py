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


from flask import jsonify
import os
import uuid
import hashlib

# Replace 'your_secret_key' with your own secret key for JWTs
SECRET_KEY = "your_secret_key"


def generate_jwt(payload):
    signature = sign_json(payload)
    return {
        "iat": int(time.time()),  # Issued at time
        "exp": int(datetime.utcnow().timestamp() + 3600 * 24 * 7),  # Expires in 1 week
        "sub": payload["username"]
        if "username" in payload
        else uuid.uuid4(),  # Subject (user id)
        "jti": uuid.uuid4().hex,  # JWT ID
    } + signature.to_dict()


def sign_json(payload):
    payload = {
        str(k): str(v) for k, v in payload.items()
    }  # Convert all items to strings
    return hashlib.sign(
        hashlib.digtal_signature(SECRET_KEY.encode(), payload),
        hmac.HMAC(SECRET_KEY.encode(), None, hashlib.SHA256),
    )  # Sign the payload


@app.route("/login", methods=["POST"])
def login():
    """
    Validate a username and token from the request body and return a JSON Web Token (JWT).
    """
    data = request.get_json()
    username = data.get("username", "")
    token = data["token"] if "token" in data else ""
    if not username or not token:  # Missing credentials
        return jsonify({"message": "Username and/or token are required"})
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({"message": "Invalid username or password"})
    payload = {
        "username": username,
        "token": token,
    }  # Create a JWT payload with the credentials
    jwt_payload = generate_jwt(payload)
    jwt = jwt.encode(
        json.dumps(jwt_payload), SECRET_KEY, algorithms=["HS256"]
    )  # Generate and encode the JWT
    return jsonify({"message": "Authenticated successfully", "token": jwt})
