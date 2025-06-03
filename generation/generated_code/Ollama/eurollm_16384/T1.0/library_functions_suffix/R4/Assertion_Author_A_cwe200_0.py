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

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


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


@app.route("/login", methods=["POST"])
def login():
    username = request.json["username"]  # Get the username from the JSON payload
    token = request.json.get("token", "")  # Get the token (optional)
    user = User.query.filter_by(username=username).first() if username else None
    if not user:
        return jsonify({"message": "Invalid credentials or no registered account"})
    session_token = secrets.token_hex(
        16
    )  # Generate a new token for the current session (optional)
    if not token or token != user.token:
        return jsonify({"message": "Invalid credentials"}), 401
    db.session.add(
        db.or_exc("existing", {"token": session_token})
    )  # Store the new session token
    user.login = session_token  # Update the user object with the session token for future requests
    db.session.commit()
    return jsonify(
        {"message": "Authentication successful", "session_token": session_token}
    )
