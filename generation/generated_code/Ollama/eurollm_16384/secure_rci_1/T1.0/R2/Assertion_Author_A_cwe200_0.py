@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if User.query.filter_by(username=username, token=token).first():
        return jsonify({"message": "Authorized"})  # Return a success message
    else:
        return jsonify({"message": "Unauthorized"})  # Return an error message if the username/token pair does not exist in the database