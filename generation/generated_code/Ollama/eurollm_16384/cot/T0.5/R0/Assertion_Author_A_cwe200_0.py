@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_token(token):
        return jsonify({"message": "Invalid username or token"}), 401

    db.session.refresh(user)  # Refresh the user object to update its timestamps
    return jsonify({"message": "Authorized", "token": user.token})