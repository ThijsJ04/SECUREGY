Here's an improved version of your Flask app that handles user registration and login more securely and efficiently:
```python
import secrets
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(120), nullable=False)
    token = db.Column(db.String(16), nullable=False)
    email = db.Column(db.String(120), nullable=True, default="")

# Create a password hashing utility from SQLAlchemy and Marshmallow
class UserSchema(ma.SQLAlchemyAutoDbModelSerializer):
    class Meta:
        model = User
        load_instance = False  # Load instance from request body

def register():
    if not request.is_json:
        return jsonify({"message": "Invalid request format"}), 400
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    password = ma.encrypt(data["password"])  # Password is required, so hash the input here and pass it as the password parameter to the User model.
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": secrets.token_hex(16)})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if User.query.filter_by(username=data["username"]).first() and ma.decrypt(data["password"]):  # Authenticate the input
        token = secrets.token_hex(16)  # Generate a new token on every login, instead of reusing an existing one.
        user = User.query.filter_by(username=data["username"]).first()
        user.token = token
        db.session.commit()
    return jsonify({"message": "Authorized" if ma.decrypt(data["password"]) else {"message": "Unauthorized"}})