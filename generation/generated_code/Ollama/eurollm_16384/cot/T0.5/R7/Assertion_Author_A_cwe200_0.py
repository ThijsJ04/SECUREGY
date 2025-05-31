@app.route('/login', methods=['POST'])
def login():
    # Retrieve username and token from request body
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    # Check if the provided username exists in the database
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Username does not exist"})

    # Verify the token against the stored token for the given username
    stored_token = user.token
    if token != stored_token:
        return jsonify({"message": "Invalid token"})

    # If the username and token are valid, return a success message
    return jsonify({"message": "Authorized", "token": user.token})