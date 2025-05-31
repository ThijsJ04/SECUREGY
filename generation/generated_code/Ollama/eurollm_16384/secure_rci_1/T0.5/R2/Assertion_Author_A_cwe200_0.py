@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not username or not token:
        return jsonify({"message": "Missing required parameters"})

    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        auth_token = secrets.token_hex(16)  # Generate a new 16-byte token for the session
        user.token = auth_token
        db.session.commit()
        return jsonify({"message": "Authorized", "auth_token": auth_token})
    else:
        return jsonify({"message": "Unauthorized"})