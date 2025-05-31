@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()
    username = data['username']  # Assuming the username is in the 'username' key of the JSON payload
    token = data['token']  # Assuming the token is in the 'token' key of the JSON payload

    if User.query.filter_by(username=username).first():
        existing_user = User.query.filter_by(username=username).first()
        return jsonify({"message": "Authorized", "token": existing_user.token})
    else:
        token = secrets.token_hex(16)  # Generate a random 16-byte token
        new_user = User(username=username, token=token)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Authorized", "token": token})