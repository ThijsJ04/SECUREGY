@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not username or not token:
        return jsonify({"message": "Unauthorized"}), 401

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Unauthorized"}), 401

    if user.token == token:
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"}), 401

if __name__ == "__main__":
    app.run(debug=True)