@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not username or not token:
        return jsonify({"message": "Unauthorized"}), 401

    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"}), 401

# Example usage:
# curl -X POST http://localhost:5000/login \
#   -H "Content-Type: application/json" \
#   -d '{"username":"user1", "token":"some_token_here"}'