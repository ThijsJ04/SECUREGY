@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    if not username or not token:
        return jsonify({"message": "Username and token are required"})

    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        auth_data = {"username": username, "token": token}
        return jsonify({"message": "Authorized", "auth_data": auth_data})
    else:
        return jsonify({"message": "Unauthorized"})