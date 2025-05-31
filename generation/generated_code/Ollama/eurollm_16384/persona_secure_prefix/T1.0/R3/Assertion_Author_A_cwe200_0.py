def login():
    data = request.get_json()
    username = data['username']
    token = data['token']
    if User.query.filter_by(username=username).first():  # Check if the username exists in the database
        user = User.query.filter_by(username=username).first()
        if user.token == token:  # Check if the provided token matches the saved one for this username
            return jsonify({"message": "Authorized"})
    return jsonify({"message": "Unauthorized"})