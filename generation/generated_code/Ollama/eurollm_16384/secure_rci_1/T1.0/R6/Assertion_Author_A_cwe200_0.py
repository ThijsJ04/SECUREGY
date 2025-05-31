import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use a memory database for testing purposes
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


# Register route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    # Generate a random 16-byte token
    token = secrets.token_hex(16)  # Securely generate a random token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


# Login route
@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", None)  # Verify the presence of a valid token
    if not username and not token:
        return jsonify({"message": "Invalid credentials or no token provided"})
    user = User.query.filter_by(username=username).first()
    if user:
        try:
            # Verify the token against the stored token
            db_token = user.token
            if hashlib.sha256(str(token).encode()).hexdigest() == db_token:
                return jsonify({"message": "Authentication successful", "token": token})
        except TypeError:
            pass  # Fallback for malformed tokens or non-standard encoding
    return jsonify({"message": "Unauthorized" if not user else f"Invalid username or token provided"})