@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({"message": "Unauthorized"})
    elif user.token == token:
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"})