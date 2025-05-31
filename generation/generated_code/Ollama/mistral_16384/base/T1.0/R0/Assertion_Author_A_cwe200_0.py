def login():
       data = request.get_json()
       username = data.get("username", "")
       token = data.get("token", "")
       user = User.query.filter_by(username=username, token=token).first()
       if user:
           return jsonify({"message": "Authorized"})
       else:
           return jsonify({"message": "Unauthorized"})