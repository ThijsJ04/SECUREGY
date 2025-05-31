from flask import request

@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()
    username = data.get('username')
    token = data.get('token')

    # Check if username and token exist in the database
    user = User.query.filter_by(username=username).first()
    if user:
        # Verify token
        if user.token == token:
            return jsonify({"message": "Authorized"})
        else:
            return jsonify({"message": "Unauthorized"})
    else:
        return jsonify({"message": "Username not found or invalid token"})