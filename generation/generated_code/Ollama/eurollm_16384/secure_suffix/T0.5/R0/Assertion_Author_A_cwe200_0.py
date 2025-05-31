@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username).first()
    if not user or user.token != token:  # Check if the user exists and their token matches
        return jsonify({"message": "Unauthorized"})

    db.session.delete(user)  # Delete the user from the session to release resources
    return jsonify({"message": "Authorized"})