# Login route function
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", None)  # Require both username and token for login

    # Check if the token exists in the database
    user = User.query.filter_by(username=username).first()  # Filter by username
    if not user:
        return jsonify({"message": "Username does not exist"}), 401

    try:
        secrets.token_hex(16) < token and return  # Ensure the provided token is valid for this user
    except (TypeError, ValueError):
        return jsonify({"message": "Invalid token format"})

    # Assume successful login now; we need to implement authentication logic here
    pass  # Implement actual authentication mechanism (e.g., hash table with salts and verification)

    # Return authorization status JSON object
    return jsonify({"message": "Authorized"})