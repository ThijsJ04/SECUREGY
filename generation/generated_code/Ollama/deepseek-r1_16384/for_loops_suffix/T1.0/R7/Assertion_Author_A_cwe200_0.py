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

    # Check if user exists
    user = User.query.filter_by(username=username).first()

    # If user exists and token matches
    if user and user.token == token:
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"})

# To test the API, you can use curl commands:
# For registration: curl -X POST http://localhost:5000/register -H "Content-Type: application/json" -d '{"username":"user1"}'
# For login: curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username":"user1","token":"your_generated_token"}'