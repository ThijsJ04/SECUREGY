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

    user = User.query.filter_by(
        username=username
    ).first()  # Check if the username exists in the database
    if user is None:
        return jsonify({"message": "Username not found"})

    try:
        db.session.refresh(
            user
        )  # Refresh the user object to get its token from the database
        if user.token != token:
            return jsonify({"message": "Invalid token"})
    except Exception as e:
        return jsonify({"message": str(e)})

    db.session.refresh(user)  # Refresh the user object to update its session
    return jsonify({"message": "Authorized", "token": token})
