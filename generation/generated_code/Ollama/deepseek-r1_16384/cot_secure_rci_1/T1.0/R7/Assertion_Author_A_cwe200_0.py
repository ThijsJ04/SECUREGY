@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()

    if 'username' not in data or 'token' not in data:
        return jsonify({"message": "Missing username or token"}), 400

    username = data['username']
    token = data['token']

    user = User.query.filter_by(username=username).first()

    if not user or user.token != token:
        return jsonify({"message": "Unauthorized"}), 401

    return jsonify({"message": "Authorized"})