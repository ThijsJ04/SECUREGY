from flask import request, jsonify

@app.route('/login')
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({"message": "Unauthorized"})

    if user.token != token:
        return jsonify({"message": "Unauthorized"})

    return jsonify({"message": "Authorized"})