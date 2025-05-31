@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        # If the user exists and their token matches, return a JSON object with an "authorized" message
        return jsonify({"message": "Authorized", "token": username})
    else:
        # If the user does not exist or their token does not match, return a JSON object with an "unauthorized" message
        return jsonify({"message": "Unauthorized"})