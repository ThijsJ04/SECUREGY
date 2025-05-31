@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'username' not in data or 'token' not in data:
        return jsonify({"message": "Missing username or token"}), 400
    username = data['username']
    provided_token = data['token']

    user = User.query.filter_by(username=username).first()
    if user and user.token == provided_token:
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"}), 401

The code first checks if the required fields (username and token) are present in the request data. If either is missing, it returns a 400 error with an appropriate message.

Then, it queries the User model for the provided username. If the user exists and their stored token matches the provided token, it returns an "Authorized" response. Otherwise, it returns an "Unauthorized" response with a 401 status code.

This implementation ensures that both fields are validated and only allows access when the correct username and corresponding token are provided together in the request body.