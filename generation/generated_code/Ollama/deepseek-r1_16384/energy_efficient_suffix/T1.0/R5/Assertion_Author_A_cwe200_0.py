@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not username or not token:
        return jsonify({"message": "Unauthorized"})

    user = User.query.filter_by(username=username).first()

    if not user or user.token != token:
        return jsonify({"message": "Unauthorized"})

    return jsonify({"message": "Authorized"})


if __name__ == '__main__':
    app.run(debug=True)