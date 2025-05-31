@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", "")
    token = data.get("token", "")

    user = User.query.filter_by(username=username, token=token).first()
    if user:
        return jsonify({"message": "Authorized"})
    else:
        return jsonify({"message": "Unauthorized"})

# To run the application:
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)