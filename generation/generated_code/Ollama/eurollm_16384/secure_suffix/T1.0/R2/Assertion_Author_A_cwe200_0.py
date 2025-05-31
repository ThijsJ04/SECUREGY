from flask import request, jsonify
import secrets

# Existing code...

@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()
    username = data.get('username', '')
    token = data['token']  # Extract the token from the JSON payload

    if User.query.filter_by(username=username).first():  # Check if username exists in the database
        user = User.query.filter_by(username=username).first()  # Get the corresponding user object
        if user and user.token == token:  # Check if the provided token matches the stored token
            return jsonify({"message": "Authorized", "token": token})  # Return a success response with the original token
        else:
            return jsonify({"message": "Unauthorized"}), 401  # Return an error message and 401 status code if authentication fails
    else:
        return jsonify({"message": "Username does not exist or token is invalid"}), 401