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
from flask_security import login_required, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)
db.create_all()  # Create the User table if it doesn't exist
migrate = Migrate(app, db)


class User(UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    password = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False, indexed=True)


class Security(object):
    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()
        if not user or user.password != password:
            return None
        return user


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, password=None, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
@login_required
def login():
    username = request.json.get("username")  # Get the username from the request body
    token = (
        User.query.filter_by(username=username).first().token
    )  # Retrieve the token for the user
    if not token:  # Check if the user exists in the database
        return jsonify({"message": "User not found"})
    authenticated, message = Security.authenticate(username, token)
    if authenticated:
        return jsonify({"message": "Authorized", "token": token})
    else:
        return jsonify({"message": "Unauthorized"})
