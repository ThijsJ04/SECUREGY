from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, refresh_token
import secrets

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)
jwt = JWTManager(app)

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
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    try:
        user = User.query.filter_by(username=username).first()
        if user and user.token == secrets.token_hex(16):  # Check the token validity
            access_token = create_access_token(identity=username)
            return jsonify({"message": "Authenticated successfully", "access_token": access_token})
        else:
            return jsonify({"message": "Invalid username or password"}), 401
    except Exception as e:
        print(e)
        return jsonify({"message": "Error authenticating"}), 500