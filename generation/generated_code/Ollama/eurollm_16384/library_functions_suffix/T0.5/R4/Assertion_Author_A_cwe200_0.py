@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()
    username = data['username']  # Assuming 'username' is a required field in the JSON payload
    token = data['token']

    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        return jsonify({"message": "Authorized", "token": token})
    else:
        return jsonify({"message": "Unauthorized"})