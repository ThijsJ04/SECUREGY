from flask import request, jsonify

@app.route('/login')
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"})