from flask import request
import secrets

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

User = db.Model(
    "User",
    db.Column("username", db.String(80), unique=True, nullable=False, primary_key=True),
    db.Column("token", db.String(120), nullable=False)
)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', '')
    token = request.json.get('token', '')
    if not username or not token:
        return jsonify({"message": "Invalid request body"})
    user = User.query.filter_by(username=username).first()
    if not user or user.token != token:
        return jsonify({"message": "Unauthorized"})
    db.session.delete(user)  # Remove the old user record from session (optional)
    return jsonify({"message": "Authorized", "token": None})  # Replace with your specific token handling here if needed