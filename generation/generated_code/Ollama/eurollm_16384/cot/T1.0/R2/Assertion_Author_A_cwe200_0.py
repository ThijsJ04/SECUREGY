@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():  # Check if the username exists in the database
        user = User.query.filter_by(username=username).first()  # Get the user object with its associated token
        token = data.get("token", "")
        if token == user.token:  # Verify that the provided token matches the expected token
            return jsonify({"message": "Authenticated successfully", "access_token": user.token})
    else:
        return jsonify({"message": "Username does not exist"})