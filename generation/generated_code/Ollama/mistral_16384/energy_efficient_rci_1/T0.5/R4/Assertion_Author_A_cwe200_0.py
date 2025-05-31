from flask import request, jsonify

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username).first()

    if not user or user.token != token:
        return jsonify({"message": "Unauthorized"})

    return jsonify({"message": "Authorized"})