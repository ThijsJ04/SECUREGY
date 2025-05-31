@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username", "")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"})
    token = secrets.token_hex(16)  # Generate a random 16-byte token
    new_user = User(username=username, token=token)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully", "token": token})


@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()
    if not 'username' in data:
        return jsonify({"error": "Missing required field 'username'"})
    if not 'token' in data:
        return jsonify({"error": "Missing required field 'token'"})
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['token']):
        token = user.token  # Fetch the registered token from the database
        return jsonify({"message": "Authorized", "token": token})
    else:
        return jsonify({"message": "Unauthorized"})