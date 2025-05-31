@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not username or not token:
        return jsonify({"message": "Invalid request, missing username/token"})

    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        session['logged_in'] = True
        return jsonify({"message": "Authorized", "session_id": str(uuid.uuid4())})
    else:
        return jsonify({"message": "Unauthorized"})