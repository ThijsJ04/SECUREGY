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
    if not data or "username" not in data or "token" not in data:
        return jsonify({"message": "Invalid input format"}), 400
    username = data["username"]
    token = data["token"]
    # Check if username and token exist in the database
    user = User.query.filter_by(username=username).first()
    if not user or user.token != token:
        return jsonify({"message": "Invalid username or token"}), 401
    # Hash the token for storage (optional)
    hashed_token = hashlib.sha256(token.encode()).hexdigest()
    db.session.commit()  # Commit any changes to the database
    return jsonify({"message": "Authenticated successfully", "token": hashed_token})
