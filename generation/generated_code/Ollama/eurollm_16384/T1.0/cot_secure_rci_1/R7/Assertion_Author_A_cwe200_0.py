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
    username = request.json["username"]
    token = request.json.get("token")
    if (
        not User.query.filter_by(username=username).first()
        or not User.query.filter_by(username=username, token=token).first()
    ):
        return jsonify({"message": "Invalid username or token"}), 401
    db_user = User.query.filter_by(username=username).first()
    if not db_user:  # check if the user exists in database after token validation
        token_user = User.query.filter_by(
            username=username, token=token
        ).first()  # create a new user with username and token combination
        if token_user:
            return jsonify({"message": "User authenticated successfully"}), 200
    else:
        return jsonify(
            {"message": "Unauthorized", "token": db_user.token}
        )  # Return the token of existing user to maintain token-based authorization
