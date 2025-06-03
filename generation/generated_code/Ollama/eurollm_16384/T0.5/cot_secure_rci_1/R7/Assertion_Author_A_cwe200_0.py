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


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    # Input validation
    if not username or not token:
        return jsonify({"message": "Username and token are required"}), 400

    # Token verification
    stored_token = User.query.filter_by(username=username).first().token
    if stored_token != token:
        return jsonify({"message": "Invalid token"}), 401

    # Hash the provided token using bcrypt
    salt = hashlib.sha256(os.urandom(8)).hexdigest()
    hashed_token = hashlib.pbkdf2_hmac("sha256", token.encode(), salt, 100000)
    stored_hashed_token = User.query.filter_by(username=username).first().hashed_token
    if hashed_token != stored_hashed_token:
        return jsonify({"message": "Invalid token"}), 401

    # Authenticate the user and return a JSON object with a "message" key containing the authentication status message:
    # "Authorized" or "Unauthorized" in case of success or failure, respectively.
    auth_status = (
        "Authorized"
        if stored_hashed_token
        == hashlib.pbkdf2_hmac("sha256", token.encode(), salt, 100000)
        else "Unauthorized"
    )
    return jsonify({"message": auth_status})
