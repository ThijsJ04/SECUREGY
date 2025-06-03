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


from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import secrets
from uuid import uuid4

# ... (rest of the code)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not username or not token:
        return jsonify({"message": "Missing required parameters"}), 400

    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({"message": "Username does not exist"}), 401

    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    expected_token = user.token + str(uuid4())[:-3] + f"_{current_time}"

    if token == expected_token:
        return jsonify(
            {
                "message": "Authorized",
                "expires": datetime.fromisoformat(f"{user.token}_{current_time}"),
            }
        )
    else:
        return jsonify({"message": "Unauthorized"}), 401
