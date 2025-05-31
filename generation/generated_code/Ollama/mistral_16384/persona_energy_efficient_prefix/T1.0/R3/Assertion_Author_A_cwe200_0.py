from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user

# Add these imports
from flask import request, jsonify

login_manager = LoginManager()

@login_manager.user_loader
def user_loader(username):
    return User.query.filter_by(username=username).first()

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
        return jsonify({"message": "Unauthorized"})