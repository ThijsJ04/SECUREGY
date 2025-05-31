@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']  # Assuming 'username' is present in the JSON object
    token = request.json.get('token', None)  # Assumes 'token' is also present in the JSON object
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Username or token does not exist"})
    current_token = user.token  # Get the stored token for this user
    if token != current_token:
        return jsonify({"message": "Invalid token"})
    return jsonify({"message": "Authenticated", "token": token})