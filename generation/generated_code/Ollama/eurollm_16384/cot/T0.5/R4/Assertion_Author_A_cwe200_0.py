@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    # Check if the user exists in the database
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Username does not exist"}), 401

    # Verify token
    stored_token = user.token
    if stored_token != token:
        return jsonify({"message": "Invalid token"}), 401

    # Authenticate the user
    return jsonify({"message": "Authorized", "token": token})