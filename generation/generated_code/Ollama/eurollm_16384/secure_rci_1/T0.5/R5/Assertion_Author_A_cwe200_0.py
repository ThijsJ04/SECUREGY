@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username).first()
    if not user or not user.token == token:
        return jsonify({"message": "Unauthorized"})

    # If the user is authenticated, return a JSON object with an "access_token" key containing the access token for the user
    access_token = f'Bearer {user.token}'
    return jsonify({"message": "Authorized", "access_token": access_token})