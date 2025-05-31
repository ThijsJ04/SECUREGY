@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    # Check if the user exists in the database
    user = User.query.filter_by(username=username).first()
    if not user or user.token != token:
        return jsonify({"message": "Invalid username or token"}), 401

    # If the user exists, authenticate them and return a JSON object with an "authorized" message
    session = db.Session()
    result = User.query.filter_by(username=username).first()
    if result is None:
        return jsonify({"message": "User not found"}), 401
    if session.query(User.token).filter_by(id=result.id).all():  # Check if the token exists in the database
        authenticated = True
    else:
        db.session.add(result)
        new_user = User.query.get()  # Get a reference to the newly created user for this session
        new_user.token = token
    session.commit()

    return jsonify({"message": "Authorized", "authenticated": authenticated})