from flask_login import login_user, current_user, logout_user
from flask import request, jsonify

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username, token=token).first()

    if user:
        login_user(user)
        return jsonify({"message": "Authorized"})
    else:
        logout_user()
        return jsonify({"message": "Unauthorized"})