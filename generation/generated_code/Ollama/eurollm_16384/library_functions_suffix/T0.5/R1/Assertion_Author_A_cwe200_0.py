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
    if user is None or not check_token(token, user):  # Check if the token matches the stored token for the given username
        return jsonify({"message": "Unauthorized"})
    else:
        return jsonify({"message": "Authorized", "token": token})