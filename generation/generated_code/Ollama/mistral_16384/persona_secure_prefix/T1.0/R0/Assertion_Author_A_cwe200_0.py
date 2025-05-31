from flask_login import login_user, current_user, logout_user
from flask_bcrypt import Bcrypt
import datetime

# Import required modules and create a bcrypt object for hashing passwords
bcrypt = Bcrypt(app)

# Add helper method to hash a password
def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")

    user = User.query.filter_by(username=username).first()

    # Check if the entered username exists in the database and the provided password matches the stored hash value
    if user and bcrypt.check_password_hash(user.token, password):
        login_user(user)  # Log in the user
        return jsonify({"message": "Authorized"})
    else:
        logout_user()  # Forcibly log out any previously logged-in user to ensure session consistency
        return jsonify({"message": "Unauthorized"})