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

# If you want to test the API endpoints, you can run this code and use tools like curl or Postman.

# Example for testing /register endpoint:
# curl -X POST http://localhost:5000/register -H "Content-Type: application/json" -d '{"username":"testuser"}'

# Example for testing /login endpoint after registration:
# curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username":"testuser","token":"<generated_token>"}'