from flask_login import UserMixin, login_user, current_user, logout_user

class ExtendedUser(User, UserMixin):
    pass

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")
    user = ExtendedUser.query.filter_by(username=username).first()
    if not user or user.password != password:
        return jsonify({"message": "Unauthorized"})
    login_user(user)
    return jsonify({"message": "Authorized", "token": user.token})