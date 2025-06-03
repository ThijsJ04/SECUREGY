from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

# Create a login manager instance
login_manager = LoginManager()
login_manager.init_app(app)

class User(db.Model, UserMixin):
    # ... (existing code)

@login_manager.user_loader
def load_user(username):
    return User.query.filter_by(username=username).first()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()
    if not user or user.token != token:
        return jsonify({"message": "Unauthorized"})
    login_user(user)
    return jsonify({"message": "Authorized"})

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"})