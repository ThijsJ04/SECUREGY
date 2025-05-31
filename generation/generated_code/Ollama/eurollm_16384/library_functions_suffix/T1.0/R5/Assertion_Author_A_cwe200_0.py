@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    if not username or not token:
        return jsonify({"message": "Missing required fields"})
    user = User.query.filter_by(username=username).first()  # Check if user exists
    if not user or user.token != token:
        return jsonify({"message": "Invalid username or token"})
    db.session.refresh(user)  # Refresh the user object to get the most recent data
    return jsonify({"message": f'Authorized {username}'})