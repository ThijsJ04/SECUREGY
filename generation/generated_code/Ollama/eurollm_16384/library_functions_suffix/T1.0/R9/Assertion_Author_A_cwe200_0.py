@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    if not username or not token:
        return jsonify({"message": "Missing username/token"}), 400
    user = User.query.filter_by(username=username).first()  # Get the user from the database based on their username
    if not user or user.token != token:  # Check if the provided token matches the one stored in the database
        return jsonify({"message": "Invalid credentials"}), 401