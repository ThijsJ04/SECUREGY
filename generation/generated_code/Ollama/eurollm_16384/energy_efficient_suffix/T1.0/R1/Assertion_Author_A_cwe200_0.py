@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()  # Find the user by username
    if not user or not user.verify_token(token):  # Check if the token is valid for the given user
        return jsonify({"message": "Unauthorized"})
    db.session.delete(user)  # Delete the user after login (to prevent multiple sessions)
    return jsonify({"message": "Authorized"})