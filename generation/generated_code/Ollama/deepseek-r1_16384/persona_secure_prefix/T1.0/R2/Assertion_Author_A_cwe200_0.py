@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    token = data.get("token")
    if User.query.filter_by(username=username, token=token).first():
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"})