from flask import Flask, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)
    token = db.Column(db.String(120), nullable=False)

@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not username:
        return jsonify({"message": "Missing required parameter 'username'"}), 400
    if not token:
        return jsonify({"message": "Missing required parameter 'token'"}), 400

    current_user = User.query.filter_by(username=username).first()  # Fetch the user from the database by username
    if not current_user or check_password_hash(current_user.password_hash, generate_password_hash(token)):  # Check if password hash matches
        return jsonify({"message": "Invalid username and/or token"})

    db.session.refresh(current_user)  # Refresh the user object for its updated `username` column
    if current_user.token != token:  # Check if the provided token matches the stored one
        return jsonify({"message": "Invalid token"})

    db.session.add(current_user)  # Add the user back to the database since we've confirmed it exists
    db.session.commit()
    return jsonify({"message": "User authenticated successfully", "token": token})