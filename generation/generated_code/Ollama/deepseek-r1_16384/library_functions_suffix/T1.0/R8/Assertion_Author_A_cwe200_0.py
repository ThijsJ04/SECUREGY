@app.route('/login', methods=['POST'])
def login():
    '''
    Get the "username" and "token" from the request body and check if the user/token combination exists in the database.
    @return: A JSON object with a "message" key containing the authentication status message:
    "Authorized" or "Unauthorized" in case of success or failure, respectively.
    '''
    data = request.get_json()
    username = data.get("username")
    token = data.get("token")

    if not username or not token:
        return jsonify({"message": "Unauthorized"}), 401

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Unauthorized"}), 401

    if user.token == token:
        return jsonify({"message": "Authorized"}), 200
    else:
        return jsonify({"message": "Unauthorized"}), 401

# Include the code after implementing the function.
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)