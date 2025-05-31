def login():
    data = request.get_json()
    username = data['username']
    token = data['token']

    user = User.query.filter_by(username=username).first()
    if user and (token == user.token):
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"})