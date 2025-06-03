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
    """
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    """
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    # Check if user exists
    user = User.query.filter_by(username=username).first()

    # If user exists and token matches
    if user and user.token == token:
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"})


# To test the API, you can use curl commands:
# For registration: curl -X POST http://localhost:5000/register -H "Content-Type: application/json" -d '{"username":"user1"}'
# For login: curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username":"user1","token":"your_generated_token"}'
