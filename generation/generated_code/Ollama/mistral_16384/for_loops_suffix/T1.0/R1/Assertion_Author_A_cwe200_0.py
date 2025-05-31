from flask import request, jsonify

@app.route('/login')
def login():
    data = request.get_json()
    username = data.get("username", "")
    password = data.get("password", "")

    user = User.query.filter_by(username=username).first()

    if not user or user.password != password:
        return jsonify({"message": "Unauthorized"})

    return jsonify({"message": "Authorized", "token": user.token})