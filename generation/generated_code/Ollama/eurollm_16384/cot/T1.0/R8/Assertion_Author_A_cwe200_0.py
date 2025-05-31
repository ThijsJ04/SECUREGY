@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", None)

    if not username or not token:
        return jsonify({"message": "Username and token are required"}), 400

    user = User.query.filter_by(username=username).first()
    if not user or user.token != token:  # Check if the user exists and has the same token as provided in the request
        return jsonify({"message": "Invalid username or token"}), 401

    db.session.refresh(user)  # Refresh the User object to get its updated token
    if user.token != token:  # Check if the token has changed (should not be able to change)
        return jsonify({"message": "Token is invalid"}), 401

    db.session.commit()  # Commit any changes made during this request
    return jsonify({"message": "User authorized", "token": user.token})