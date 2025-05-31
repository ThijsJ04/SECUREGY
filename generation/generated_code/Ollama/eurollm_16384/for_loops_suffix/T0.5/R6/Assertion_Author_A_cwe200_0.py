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
    data = request.get_json()
    username = data.get("username")
    token = data.get("token")
    if not username or not token:
        return jsonify({"message": "Username and/or token are missing"})
    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        # Check if the token is valid (e.g., expired or revoked)
        pass  # Implement token validation logic here
        return jsonify({"message": "Authorized", "token": token})
    else:
        return jsonify({"message": "Unauthorized"})