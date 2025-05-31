@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    if not username or not token:
        return jsonify({"message": "Invalid request body"})
    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        session_data = {
            'username': username,
            'token': token,
        }
        db.session.add(session_data)
        db.session.commit()
        return jsonify({"message": "Authenticated successfully"})
    else:
        return jsonify({"message": "Invalid username or token"})