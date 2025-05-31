from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
import secrets

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
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not username or not token:
        return jsonify({"message": "Missing required fields"})

    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        auth_message = {"message": "Authorized", "token": token}
        return jsonify(auth_message)
    else:
        auth_message = {"message": "Unauthorized"}
        return jsonify(auth_message)