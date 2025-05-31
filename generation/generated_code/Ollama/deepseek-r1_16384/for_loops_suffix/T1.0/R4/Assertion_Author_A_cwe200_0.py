@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    if User.query.filter_by(username=username, token=token).count() > 0:
        return jsonify({"message": "Authorized"})
    return jsonify({"message": "Unauthorized"})