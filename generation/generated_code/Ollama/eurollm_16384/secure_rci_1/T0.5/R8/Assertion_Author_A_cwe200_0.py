@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not username or not token:
        return jsonify({"message": "Invalid input, both username and token are required."}), 400

    user = User.query.filter_by(username=username).first()  # Check if the user exists in the database
    if not user or user.token != token:  # Check if the provided token matches the stored one
        return jsonify({"message": "Invalid username or token."}), 401

    session_data = {"username": username, "token": token}
    return jsonify({"message": "Authorized", **session_data})  # Return a JSON object with the user's information