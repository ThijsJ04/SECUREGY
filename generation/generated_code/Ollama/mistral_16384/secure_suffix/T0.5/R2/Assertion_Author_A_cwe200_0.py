from flask_login import login_user, current_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Unauthorized"})

    login_user(user)
    return jsonify({"message": "Authorized"})