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

    if not username or not token:
        return jsonify({"message": "Missing required parameters"})

    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        auth_token = secrets.token_hex(16)  # Generate a new authentication token
        user.auth_token = auth_token
        db.session.commit()
        return jsonify({"message": "Authorized", "auth_token": auth_token})
    else:
        return jsonify({"message": "Unauthorized"})
