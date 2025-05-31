from functools import wraps
import re
import hashlib

def require_token(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        data = request.get_json()
        token = data.get("token", "")
        user = User.query.filter_by(token=token).first()
        if not user:
            return jsonify({"message": "Unauthorized"})
        return func(*args, **kwargs)
    return decorated

@app.route('/login', methods=['POST'])
@require_token
def login():
    data = request.get_json()
    username = data.get("username", "")
    existing_user = User.query.filter_by(username=username).first()
    if not existing_user:
        return jsonify({"message": "User does not exist"})

    if existing_user.token != request.json['token']:
        return jsonify({"message": "Invalid token"})

    return jsonify({"message": "Authorized"})