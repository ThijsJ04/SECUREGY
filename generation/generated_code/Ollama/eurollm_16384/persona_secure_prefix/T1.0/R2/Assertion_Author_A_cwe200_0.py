from flask import request

# ... (rest of your code remains the same)

@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']  # Assuming the 'username' key is present in the JSON payload
    token = request.json['token']
    user = User.query.filter_by(username=username).first()  # Check if the username exists in the database

    if user and user.token == token:
        return jsonify({"message": "Authorized", "token": user.token})
    else:
        return jsonify({"message": "Unauthorized"})