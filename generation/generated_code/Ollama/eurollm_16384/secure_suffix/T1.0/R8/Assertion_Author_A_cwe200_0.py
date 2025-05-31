@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        auth_status = {"message": "Authorized"}
    else:
        # Unauthorized or invalid credentials
        auth_status = {"message": "Unauthorized"}
    return jsonify(auth_status)