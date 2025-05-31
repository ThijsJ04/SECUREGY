@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()  # Check if the username exists in the database
    if not user:
        return jsonify({"message": "Username does not exist"}), 401
    token_exists = db.session.query(User).filter_by(token=token).first()  # Check if the token exists in the database
    if not token_exists:
        return jsonify({"message": "Invalid token"}), 401
    session = db.Session()
    auth_session = session.query(User).filter_by(username=username, token=token).first()  # Check if the user has a valid session
    if not auth_session:
        return jsonify({"message": "Unauthorized"}), 401
    db.session.close()
    return jsonify({"message": "Authorized", "token": token})