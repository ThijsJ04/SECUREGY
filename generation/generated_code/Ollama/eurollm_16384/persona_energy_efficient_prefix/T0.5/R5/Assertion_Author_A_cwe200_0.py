@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username).first()  # Fetch the user from the database

    if not user or user.token != token:  # Check if the user exists and their token matches
        return jsonify({"message": "Unauthorized"})

    db.session.delete(user)  # Remove the user's record from the database to prevent unauthorized access
    return jsonify({"message": "Authorized", "token": token})