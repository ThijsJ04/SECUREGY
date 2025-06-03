from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

# Initialize the Flask-Login extension
login_manager = LoginManager()
login_manager.init_app(app)

class User(db.Model, UserMixin):
    # ... existing code

@login_manager.request_loader
def load_user_from_request(request):
    data = request.get_json()
    if not data or "token" not in data:
        return None
    user = User.query.filter_by(token=data["token"]).first()
    return user

@login.user_loader
def load_user_from_id(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = db.session.query(User).filter_by(username=username).first().token if User.query.filter_by(username=username).first() else None
    if not token:
        return jsonify({"message": "Invalid credentials"})
    user = load_user_from_token(token)
    login_user(user, remember=True)
    return jsonify({"message": "Authorized"})

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out"})