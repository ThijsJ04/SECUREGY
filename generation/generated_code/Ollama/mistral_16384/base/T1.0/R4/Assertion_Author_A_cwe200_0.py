from flask import request, jsonify

# Helper function to verify user authentication
def authenticate(username, token):
    user = User.query.filter_by(username=username).first()
    return user and user.token == token

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not authenticate(username, token):
        return jsonify({"message": "Unauthorized"})

    return jsonify({"message": "Authorized"})