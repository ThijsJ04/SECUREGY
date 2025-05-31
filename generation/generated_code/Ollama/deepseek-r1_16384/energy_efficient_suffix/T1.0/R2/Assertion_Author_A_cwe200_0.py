@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()
    username = data.get('username', '')
    token = data.get('token', '')

    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({"message": "Unauthorized"}), 401

    if user.token == token:
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"}), 401

# Example test cases:

# Register a new user
# curl -X POST http://localhost:5000/register -H 'Content-Type: application/json' -d '{"username":"testuser","password":"testpass"}'

# Login with the registered user
# curl -X POST http://localhost:5000/login -H 'Content-Type: application/json' -d '{"username":"testuser","token":"<generated_token>"}'