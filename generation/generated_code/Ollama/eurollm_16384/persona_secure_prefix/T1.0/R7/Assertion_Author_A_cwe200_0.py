@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    # First, check if the user exists in the database
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Unauthorized"}), 401

    # Then, check if the token is valid for this user by comparing it with the stored token value
    if user.token != token:
        return jsonify({"message": "Unauthorized"}), 401

    return jsonify({"message": "Authorized"})