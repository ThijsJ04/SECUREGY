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
from werkzeug.security import safe_str_cmp, generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password_hash = db.Column(db.String(128))
    token = db.Column(db.String(120), nullable=False)


# Add the check_password_for_user function to the User class as a static method
User.check_password_for_user = staticmethod(
    lambda user, password: check_password_hash(user.password_hash, password)
)

app.secret_key = secrets.token_hex(32)  # Set secret key for flask sessions


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    password = generate_password_hash(
        data.get("password", "")
    )  # Hash the provided password
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, password_hash=password, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    user = User.query.filter_by(username=username).first()
    if not user or not User.check_password_for_user(user, password):
        return jsonify({"message": "Unauthorized"})
    return jsonify({"message": "Authorized", "token": user.token})
