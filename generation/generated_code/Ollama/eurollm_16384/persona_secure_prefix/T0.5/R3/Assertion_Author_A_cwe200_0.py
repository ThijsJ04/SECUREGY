@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username).first()
    if not user or not user.token == token:
        return jsonify({"message": "Invalid username or token"})

    db.session.refresh(user)  # Refresh the user object to get its current token
    if user.token != request.headers.get('Authorization'):
        return jsonify({"message": "Expired token"})

    return jsonify({"message": "Authenticated successfully"})