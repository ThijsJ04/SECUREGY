@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    # Check if the user exists in the database
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Invalid username or password"})

    # Validate the token
    try:
        secret_key = "your_secret_key"  # Replace with your actual secret key
        session_token = user.token
        hashed_session_token = str(secrets.hmac(secret_key, session_token, hashlib.sha256))[:32]
        if token != hashed_session_token:
            return jsonify({"message": "Invalid token or expired session"})
    except ValueError:
        return jsonify({"message": "Invalid token or expired session"})

    # Store the session token in the database for later use (if needed)
    db.session.add(user)  # This will create a new entry if user is not found yet, and commit all changes afterwards
    db.session.commit()

    return jsonify({"message": "User authenticated successfully", "token": hashed_session_token})