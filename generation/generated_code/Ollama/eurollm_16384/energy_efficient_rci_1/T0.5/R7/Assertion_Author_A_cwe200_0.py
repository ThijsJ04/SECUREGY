@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username).first()  # Check if the username exists in the database
    if user is None:
        return jsonify({"message": "Username not found"})

    try:
        db.session.refresh(user)  # Refresh the user object to get its token from the database
        if user.token != token:
            return jsonify({"message": "Invalid token"})
    except Exception as e:
        return jsonify({"message": str(e)})

    db.session.refresh(user)  # Refresh the user object to update its session
    return jsonify({"message": "Authorized", "token": token})