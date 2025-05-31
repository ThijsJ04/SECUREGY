@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    if not username or not token:
        return jsonify({"message": "Both username and token are required"}), 400

    user = User.query.filter_by(username=username).first()

    if user and user.token == token:
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"}), 401

# Example usage:

if __name__ == '__main__':
    app.run(debug=True)