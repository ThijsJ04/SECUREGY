from flask_login import login_user, current_user, logout_user
from flask import jsonify

@app.route('/login')
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username, token=token).first()
    if not user:
        return jsonify({"message": "Unauthorized"})

    login_user(user)
    return jsonify({"message": "Authorized"})