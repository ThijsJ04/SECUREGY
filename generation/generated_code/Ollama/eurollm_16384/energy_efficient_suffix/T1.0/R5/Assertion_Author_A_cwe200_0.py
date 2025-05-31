@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()  # Check if the username exists in the database
    if user is None:
        return jsonify({"message": "Invalid username or password"})
    token_check = User.query.filter_by(token=token).first()
    if token_check is None:  # Check if the token exists in the database
        return jsonify({"message": "Invalid token"})
    user.token = None  # Mark the token as used after successful authentication
    db.session.commit()  # Commit changes to the database
    return jsonify({"message": "Authorized", "token": token_check.token})