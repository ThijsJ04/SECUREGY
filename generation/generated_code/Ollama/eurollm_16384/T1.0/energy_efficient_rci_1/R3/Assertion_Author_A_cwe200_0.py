import secrets
from datetime import timedelta
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(
        db.String(120), nullable=False
    )  # Refresh token is not needed for demo
    refresh_token = db.Column(
        db.String(120)
    )  # Replace with actual refresh token generation in production code
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# Helper function to generate a random 60-minute expiration time for the login token
def gen_expiration_time():
    return datetime.utcnow() + timedelta(
        minutes=60
    )  # Replace with actual expiration time in production code


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    refresh_token = secrets.token_hex(
        32
    )  # Replace with actual refresh token generation in production code
    token = secrets.token_hex(16)  # Generate a random 16-byte login token
    new_user = User(
        username=username,
        token=token,
        created_at=datetime.utcnow(),
        refresh_token=refresh_token,
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(
        {
            "message": "User registered successfully",
            "login_token": token,
            "expiration_time": gen_expiration_time(),
        }
    )


@app.route("/logout")
def logout():
    user = User.query.filter_by(
        username=request.args.get("username")
    ).first()  # Retrieve user by username from the query parameters
    if user:
        user.token = (
            None  # Reset token to None in case of a forced or session expiration
        )
        db.session.commit()
        return jsonify({"message": "Logged out successfully"})
    else:
        return jsonify(
            {"message": "No user found for logout"}
        ), 401  # Return error in case of unauthorized access


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    if not User.query.filter_by(username=username).first():
        return jsonify({"message": "Username does not exist"})
    token, expiration_time = get_login_token(
        data
    )  # Retrieve login token from the request body and verify its validity
    if (
        token is None or datetime.now() >= expiration_time
    ):  # Check if the login token has expired
        return jsonify({"message": "Login token has expired"})
    user = User.query.filter_by(
        username=username
    ).first()  # Retrieve user by username from the query parameters
    if not user:
        return jsonify(
            {"message": "No user found for login"}
        ), 401  # Return error in case of unauthorized access
    auth_status = authenticate(token, user)  # Authenticate user using their login token
    if not auth_status:
        return jsonify({"message": "Invalid login token"})
    user.expires_at = (
        gen_expiration_time()
    )  # Set a new expiration time for the login token
    db.session.commit()
    return jsonify(
        {"message": "Authenticated successfully", "refresh_token": user.refresh_token}
    )
