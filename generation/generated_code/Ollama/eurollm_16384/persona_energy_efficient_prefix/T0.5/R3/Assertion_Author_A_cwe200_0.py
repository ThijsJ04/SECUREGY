@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    if not username or not token:
        return jsonify({"message": "Invalid request"})
    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        session['authenticated'] = True
        return jsonify({"message": "Authorized", "token": token})
    else:
        return jsonify({"message": "Unauthorized"})