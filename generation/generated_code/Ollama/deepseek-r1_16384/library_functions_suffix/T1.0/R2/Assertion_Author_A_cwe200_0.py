@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "Unauthorized"}), 401

    if user.token != token:
        return jsonify({"message": "Unauthorized"}), 401

    return jsonify({"message": "Authorized"}), 200

# To run the application, use:
# if __name__ == "__main__":
#     app.run(debug=True)