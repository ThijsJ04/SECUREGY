@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()
    if not user or user.token != token:  # Check if the username and token are valid
        return jsonify({"message": "Unauthorized"})
    db.session.delete(user)  # Remove the old session
    return jsonify({"message": "Authorized", "token": token, "expiration_time": None})