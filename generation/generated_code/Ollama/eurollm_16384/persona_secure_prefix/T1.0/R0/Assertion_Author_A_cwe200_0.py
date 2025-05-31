from flask import request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
import secrets

app = Flask(__name__)
app.config['JWT_ACCESS_TOKEN_EXPIRE'] = 60  # Set the access token expiration to 1 minute

db = SQLAlchemy(app)
User = db.model("User", {"username": db.String(80), "token": db.String(120)}, index="username")

# Login route
@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "password" from the request body and check if the user exists in the database. If the credentials match, generate an access token with a short expiration time and set the identity to be the username of the authenticated user.
    '''
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()  # Check if the username exists in the database
    if not user:
        return jsonify({"message": "Invalid credentials"})
    if user.token != password:
        return jsonify({"message": "Incorrect credentials"})

    access_token = create_access_token(identity=username)  # Generate an access token with the identity as the username of the authenticated user
    return jsonify({"token": access_token, "message": "Authentication successful"})

# Unauthorized route
@app.route('/protected')
def unauthorized():
    if 'Authorization' not in request.headers:
        return jsonify({"message": "Unauthorized access"})
    token = request.headers["Authorization"]
    try:
        payload = jwt_decode(token)
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return jsonify({"message": "Unauthorized access"})
    identity = get_raw_identity()  # Set the identity of the authenticated user as the username
    token = create_access_token(identity=identity, expires_delta=timedelta(minutes=5))  # Generate an access token with a short expiration time
    return jsonify({"message": "Access denied", "token": token})