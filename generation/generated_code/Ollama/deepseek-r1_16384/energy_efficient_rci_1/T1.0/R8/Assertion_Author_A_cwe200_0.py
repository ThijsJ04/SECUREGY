@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")
    user = User.query.filter_by(username=username).first()
    if user and user.token == token:
        return jsonify({"message": "Authorized"}), 200
    else:
        return jsonify({"message": "Unauthorized"}), 401

# To run the application, execute this script and visit http://localhost:5000 in your browser.