from flask import request, jsonify
from flask_security import Security
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)
security = Security(app)
bcrypt = Bcrypt(app)

# User model
class User(db.Model, security.UserMixin):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(60), nullable=False)

# User authentication
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", "")
    password = request.json.get("password", "")
    user = User.query.filter_by(username=username).first()
    if not user or bcrypt.check_password_hash(user.password, password):
        # Generate a token and return it as the response
        token = secrets.token_hex(16)
        response = jsonify({"message": "Authenticated successfully", "token": token})
        response.headers["Authorization"] = f"Bearer {token}"  # Set the token as a bearer token
        return response
    else:
        return jsonify({"error": "Invalid username or password"}), 401