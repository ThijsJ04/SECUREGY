import secrets
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    # ... (same as before)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Get the JSON payload from the request body
    username = data.get("username", "")  # Extract the username from the JSON payload
    token = data.get("token", "")  # Extract the token from the JSON payload (optional)

    user = User.query.filter_by(username=username).first()  # Find a user with the provided username
    if not user:
        return jsonify({"message": "Invalid username or no user found"})

    current_token = user.token
    if token and current_token != token:
        return jsonify({"message": "Invalid token"})

    # If the username and token match, return a JSON object with an "authorized" message
    return jsonify({"message": "Authorized", "token": user.token})