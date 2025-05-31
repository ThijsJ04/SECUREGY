@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not username or not token:
        return jsonify({"message": "Invalid input"})

    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        session_token = user.token  # Assign the token to a session variable for subsequent requests
        return jsonify({"message": "Authorized", "session_token": session_token})
    else:
        return jsonify({"message": "Unauthorized"})