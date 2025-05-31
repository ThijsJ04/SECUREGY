import secrets
from flask import request, jsonify, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(256), nullable=False)  # Use a secure hashed password in the database
    is_active = db.Column(db.Boolean(), default=False)  # Flag to indicate user is active or not
    token = db.Column(db.String(120), nullable=False, unique=True)  # Token should be unique

    @classmethod
    def verify_token(cls, token):
        return User.query.filter_by(token=token).first() is not None

    @staticmethod
    def _generate_password(length):
        password = ''.join([secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for _ in range(length)])
        return password

    @staticmethod
    def create_token():
        password = User._generate_password(128)  # Generate a secure 128-character password
        salt = ''.join([secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for _ in range(32)])  # Salt is 32 characters
        hashed_password = generate_password_hash((password + salt), method='sha256', salt=salt, safe=False)
        token = User.query.filter_by(username=password).first().token  # Set the token based on the username
        return {'username': password, 'token': hashed_password}

    @staticmethod
    def login(token):
        try:
            User.query.filter_by(token=token).first()  # Try to find a matching user by token
            current_user = User.query.filter_by(token=token).first()
            if check_password_hash(current_user.password, token):  # Check if the password is valid
                flash('Login successful!', 'success')
                session['username'] = current_user.username  # Set the username in session for CSRF protection
                return redirect('/')
            else:
                flash('Invalid token or password!', 'danger')
        except Exception as e:
            db.session.rollback()
            flash('Something went wrong: {}'.format(e), 'error')
            return redirect('/login')  # Return to login page after rolling back changes

    @staticmethod
    def update_user():
        data = request.get_json()
        if not User.verify_token(data.get('token', None)):
            flash('Invalid token!')
            return redirect('/login')
        if 'username' in data:  # Check if username is updated
            current_user = User.query.filter_by(username=data['username']).first()
            db.session.delete(current_user)  # Remove the user from session and database
            User.query.filter_by(username=data['username']).update({'is_active': False})  # Flag as inactive
        current_user = User(token=data.get('token', None))  # Create a new user if none exists for the provided token
        if 'username' in data and User.query.filter_by(username=data['username']).first():
            current_user = User.query.filter_by(username=data['username']).first()  # Update existing user
        db.session.add(current_user)  # Add or update the user in the database
        flash('User updated successfully!', 'success')
        db.session.commit()

    @staticmethod
    def delete_user():
        token = request.args.get('token', None, type=str)  # Get the token from query string
        data = {'token': token}
        User.query.filter_by(**data).update({'is_active': False})  # Flag the user as inactive and remove from session
        User.query.filter_by(username=token).delete()  # Remove the user from the database if no other existing users match the token
        db.session.commit()
        flash('User deleted successfully!', 'success')

    @staticmethod
    def update_password():
        data = request.get_json()
        if not User.verify_token(data.get('token', None)):
            flash('Invalid token!')
            return redirect('/login')
        new_password = generate_password_hash(data['new_password'], method='sha256', safe=False)  # Hash the new password using SHA-256 algorithm
        current_user = User.query.filter_by(token=data['token']).first()
        if not check_password_hash(current_user.password, data['new_password']):  # Check if the new password is valid
            flash('Invalid old or new password!')
            return redirect('/login')
        current_user.password = <PASSWORD>_hash(data['new_password'], safe=False)  # Update the user's hashed password in the database
        flash('Password updated successfully!', 'success')
        db.session.commit()

    @staticmethod
    def update_token():
        data = request.get_json()
        if not User.verify_token(data.get('token', None)):
            flash('Invalid token!')
            return redirect('/login')
        current_user = User.query.filter_by(token=data['new_token']).first()  # Get the user with the new token if any
        if not current_user:  # No existing user found for the new token
            token = User.create_token()  # Create a new user and set their token
            flash('Token updated successfully!', 'success')
        else:
            current_user.token = data['new_token']  # Update the user's token in the database
        db.session.commit()