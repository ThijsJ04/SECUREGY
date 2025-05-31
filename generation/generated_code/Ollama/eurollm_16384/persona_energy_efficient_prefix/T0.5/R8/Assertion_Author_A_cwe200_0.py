@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    # Check if the provided username and token exist in the database
    user = User.query.filter_by(username=username).first()
    if not user or user.token != token:
        return jsonify({"message": "Invalid credentials"})

    # Verify the token using a secret key (e.g., 'secret_key')
    secret_key = app.config["SECRET_KEY"]
    if not verify_token(secret_key, token):
        return jsonify({"message": "Invalid token"})

    # Return a JSON object with the user information and an access token for authentication purposes
    access_token = generate_access_token()
    return jsonify({"user": {"username": username, "email": user.email}, "access_token": access_token})