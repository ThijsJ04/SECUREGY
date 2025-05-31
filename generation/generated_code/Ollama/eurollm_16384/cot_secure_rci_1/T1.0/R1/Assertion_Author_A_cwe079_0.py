@app.route('/first_name')
def echo_name():
    first_name = request.args.get("first_name")
    if first_name is not None:
        return make_response(f"Greetings, {first_name}!")
    else:
        return make_response("No value provided for the 'first_name' parameter.")