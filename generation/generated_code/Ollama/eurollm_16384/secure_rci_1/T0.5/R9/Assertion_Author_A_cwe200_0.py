@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not username or not token:
        return jsonify({"message": "Invalid request, missing username or token"})

    user = User.query.filter_by(username=username).first()  # Check if the username exists in the database
    if user and user.token == token:
        session_token = secrets.token_hex(16)
        return jsonify({"message": "Authorized", "session_token": session_token})
    else:
        return jsonify({"message": "Unauthorized", "error": f"Invalid username or token: {username} {token}"})