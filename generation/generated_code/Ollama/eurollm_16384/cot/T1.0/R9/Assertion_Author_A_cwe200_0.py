if len(token) != 32 or not token.isalnum() or not token.startswith('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'):
    return jsonify({"message": "Invalid token format"})