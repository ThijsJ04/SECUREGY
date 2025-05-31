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

    if not username or not token:
        return jsonify({"message": "Missing required parameters"}), 400

    user = User.query.filter_by(username=username).first()  # Check if the user exists in the database
    if not user:
        return jsonify({"message": "Invalid username or token"})

    current_token = user.token
    if token != current_token:
        return jsonify({"message": "Invalid token"})

    return jsonify({"message": "Authorized", "token": token})