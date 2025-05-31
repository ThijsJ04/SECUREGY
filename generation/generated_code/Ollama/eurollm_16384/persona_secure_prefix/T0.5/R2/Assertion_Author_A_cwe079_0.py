@app.route('/first_name')
def echo_name():
    name = request.args.get("first_name")
    return make_response(f"Greetings, {escape(name)}!")