def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        # Check password or verify the token using a secret (not shown)
        authenticated_user = user
        return jsonify({"message": "Authorized", "authenticated_user": authenticated_user})
    else:
        return jsonify({"message": "Unauthorized"})