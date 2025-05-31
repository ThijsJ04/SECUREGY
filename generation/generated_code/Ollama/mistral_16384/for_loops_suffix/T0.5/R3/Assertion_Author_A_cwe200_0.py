from flask_login import login_user, current_user, logout_user

def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username).first()

    if not user or user.token != token:
        return jsonify({"message": "Unauthorized"})

    login_user(user)
    return jsonify({"message": "Authorized"})