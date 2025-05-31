@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if User.query.filter_by(username=username, token=token).first():
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"})

# Example usage:
# To test the API endpoints, you can run a simple HTTP server and make requests to http://localhost:5000/register or http://localhost:5000/login
# You can use tools like curl or Postman to send requests with appropriate JSON bodies.