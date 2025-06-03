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

    user = User.query.filter_by(username=username, token=token).first()

    if user:
        return jsonify({"message": "Authorized"}), 200
    else:
        return jsonify({"message": "Unauthorized"}), 401


# If you want to test the API endpoints, you can run this code and use tools like curl or Postman.

# Example for testing /register endpoint:
# curl -X POST http://localhost:5000/register -H "Content-Type: application/json" -d '{"username":"testuser"}'

# Example for testing /login endpoint after registration:
# curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username":"testuser","token":"<generated_token>"}'
