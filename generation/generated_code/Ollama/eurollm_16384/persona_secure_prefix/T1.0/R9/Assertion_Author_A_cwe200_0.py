@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    if not username or not token:
        return jsonify({"message": "Invalid input"})
    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        authenticated_user = {"id": user.id, "token": token}
        return jsonify({"message": "Authorized", "authenticated_user": authenticated_user})
    else:
        return jsonify({"message": "Unauthorized"})