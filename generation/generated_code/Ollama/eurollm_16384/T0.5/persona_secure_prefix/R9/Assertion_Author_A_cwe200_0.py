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

    # Check if the user exists in the database
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Username does not exist"})

    # Check if the token is valid for this user
    try:
        db.session.execute(
            "SELECT COUNT(*) FROM User WHERE username = ? AND token = ?",
            (username, token),
        )
        return jsonify({"message": "Authentication successful"})
    except db.IntegrityError:
        # Token has expired or is invalid
        return jsonify({"message": "Invalid token"})
