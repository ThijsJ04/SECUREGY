from flask import jsonify
import secrets
from datetime import timedelta

# ... (rest of your code remains the same)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    try:
        # Validate user input
        db.session.query(User).filter_by(username=username).first()  # Check if username exists in the database
    except Exception as e:
        return jsonify({"message": str(e)})

    try:
        # Verify token validity (using a library like python-jose or implementing your own logic)
        token_is_valid = verify_token(token, username)  # Return True/False based on token validation
    except Exception as e:
        return jsonify({"message": str(e)})

    try:
        # Authenticate user by checking their username in the database
        db.session.query(User).filter_by(username=username).first()  # Check if username exists and is valid
    except Exception as e:
        return jsonify({"message": str(e)})

    db.session.commit()

    if token_is_valid and username:
        token = secrets.token_hex(16)  # Generate a new 16-byte token for the user session
        return jsonify({"message": "User authenticated successfully", "token": token})
    else:
        return jsonify({"message": "Unauthorized"})