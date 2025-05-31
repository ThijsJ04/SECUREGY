@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username, token=token).first()

    if user:
        return jsonify({"message": "Authorized"}), 200
    else:
        return jsonify({"message": "Unauthorized"}), 401

# Example usage:
# curl -X POST http://localhost:5000/login \
#   -H "Content-Type: application/json" \
#   -d '{"username":"testuser", "token":"some_token_here"}'