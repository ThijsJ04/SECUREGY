from flask_login import login_user, current_user, logout_user
from flask_bcrypt import Bcrypt
import jsonify

bcrypt = Bcrypt()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    user = User.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.token, password):
        login_user(user)
        return jsonify({"message": "Authorized"})
    else:
        logout_user()
        return jsonify({"message": "Unauthorized"})