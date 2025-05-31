from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user

# Initialize the Flask-Login extension
login_manager = LoginManager()
login_manager.init_app(app)

# Modify the User class to inherit from UserMixin
class User(db.Model, UserMixin):
    # ... existing code ...

@login_manager.user_loader
def load_user(username):
    return User.query.filter_by(username=username).first()

# Modify the login function to handle user authentication
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")

    user = User.query.filter_by(username=username).first()
    if not user or user.password != password:  # Check the password here
        return jsonify({"message": "Unauthorized"})

    login_user(user)  # Authenticate the user and set current_user
    return jsonify({"message": "Authorized"})