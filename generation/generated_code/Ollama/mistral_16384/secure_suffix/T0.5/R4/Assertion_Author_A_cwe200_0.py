from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

# Add these imports to the top of your file
from werkzeug.security import safe_str_cmp, generate_password_hash, check_password_hash

# Initialize Flask-Login instance
login_manager = LoginManager()
login_manager.init_app(app)

# Modify User class to include methods for authentication and authorization
class User(db.Model, UserMixin):
    # ... (existing code remains unchanged)

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

# Modify login function to handle authentication and authorization
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")

    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return jsonify({"message": "Unauthorized"})

    login_user(user)
    return jsonify({"message": "Authorized", "token": user.token})