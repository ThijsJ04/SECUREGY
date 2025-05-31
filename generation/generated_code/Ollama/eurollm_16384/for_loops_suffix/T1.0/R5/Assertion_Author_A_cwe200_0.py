import secrets
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    # ... (same as before)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()
    if not user or user.token != token:
        return jsonify({"message": "Unauthorized"})
    # Check if the user's token is still valid by verifying it against a random one-time verification code
    db.session.add(User(username=username, token=secrets.token_hex(16)))  # Generate a new 16-byte token for verification
    return jsonify({"message": "Authorized", "verificationCode": secrets.token_hex(8)})