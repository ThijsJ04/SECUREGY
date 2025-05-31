from flask_login import LoginManager, login_user, current_user, logout_user
from flask_bcrypt import Bcrypt

# Initialize Flask-Login and Flask-BCrypt
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)

@login_manager.user_loader
def load_user(username):
    return User.query.filter_by(username=username).first()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User not found"})

    if bcrypt.check_password_hash(user.token, password):
        login_user(user)
        return jsonify({"message": "Authorized"})
    else:
        logout_user()
        return jsonify({"message": "Unauthorized"})