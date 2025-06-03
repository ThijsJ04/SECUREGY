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


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from secrets import token_hex

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


@app.route("/register", methods=["POST"])
def register():
    # Get the JSON data from the request body
    data = request.get_json()
    username = data.get("username", "")

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})

    # Generate a random 16-byte token and create a new user
    token = token_hex(length=16)  # Secure random function for generating tokens
    new_user = User(username=username, token=token)

    # Add the new user to the database session and commit it
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
def login():
    """
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    """
    # Get the data from the request body and store them as query parameters for simplicity
    params = request.json_encoded_form_data.copy()

    # Check if both username and token are provided
    if "username" not in params or "token" not in params:
        return jsonify({"message": "Invalid input, provide 'username' and 'token'"})

    username = params.get("username")
    token = params.get("token")

    # Check if the username/token combination exists in the database
    existing_user = User.query.filter_by(username=username, token=token).first()
    if not existing_user:
        return jsonify({"message": "Invalid credentials"})

    # Authenticate the user and return a success message with their ID if authenticated
    db.session.query(User).filter_by(
        username=existing_user.username, token=existing_user.token
    ).first()
    return jsonify({"message": "Authenticated successfully", "id": existing_user.id})
