@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()
    if not data or 'username' not in data or 'token' not in data:
        return jsonify({"message": "Invalid input format"}), 400
    username = data['username']
    token = data['token']
    # Check if username and token exist in the database
    user = User.query.filter_by(username=username).first()
    if not user or user.token != token:
        return jsonify({"message": "Invalid username or token"}), 401
    # Hash the token for storage (optional)
    hashed_token = hashlib.sha256(token.encode()).hexdigest()
    db.session.commit()  # Commit any changes to the database
    return jsonify({"message": "Authenticated successfully", "token": hashed_token})