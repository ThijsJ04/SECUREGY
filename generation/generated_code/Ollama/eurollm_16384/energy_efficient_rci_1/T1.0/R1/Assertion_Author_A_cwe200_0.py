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
    if not isinstance(request.json, dict) or 'username' not in request.json:
        return jsonify({"message": "Invalid request data"}), 400

    try:
        data = request.get_json()
        username = data['username']
    except (KeyError, ValueError):
        return jsonify({"message": "Username is required"}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    try:
        db.session.commit()
        return jsonify({"message": "User registered successfully", "token": token})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    return None  # Return no response on commit failure for simplicity