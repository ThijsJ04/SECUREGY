@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not username or not token:
        return jsonify({"message": "Invalid request body"}), 400

    user = User.query.filter_by(username=username).first()  # Retrieve the user from the database
    if not user or user.token != token:  # Check if the username and token match
        return jsonify({"message": "Invalid credentials"}), 401

    session_token = secrets.token_hex(32)  # Generate a new session token for security purposes
    user.session_token = session_token
    db.session.commit()

    return jsonify({"message": "Authenticated successfully", "session_token": session_token})