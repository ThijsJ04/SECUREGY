@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username).first()

    if not user or not user.token == token:
        return jsonify({"message": "Invalid credentials or username does not exist"}), 401

    db.session.refresh(user)  # Refresh the User object to get a fresh reference to its attributes
    if not user.is_active():
        return jsonify({"message": "Account is inactive"}), 403

    return jsonify({"message": "Authorized"})