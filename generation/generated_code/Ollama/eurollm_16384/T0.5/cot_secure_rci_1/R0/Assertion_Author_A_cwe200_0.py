import secrets

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
db = SQLAlchemy(app)


# User model
class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", None)
    if not username or not token:
        return jsonify({"message": "Invalid request body"}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Username does not exist"})

    token_exists = db.session.query(User).filter_by(token=token).first() is not None
    if not token_exists:
        current_time = int(round(time.time() * 1000))  # Convert to Unix timestamp
        expiration_time = current_time + User.TOKEN_EXPIRATION_SECONDS
        db.session.add(User(token=secrets.token_hex(16), expires_at=expiration_time))
        db.session.commit()  # Commit the session to persist the token and expiration time
    else:
        user.expires_at = current_time + User.TOKEN_EXPIRATION_SECONDS
    db.session.commit()

    return jsonify({"message": "Authenticated successfully", "token": token})
