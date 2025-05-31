@app.route('/first_name', methods=['GET'])
def echo_name():
    first_name = request.args.get('first_name')
    if not first_name:
        return make_response("No first name provided.", 400)
    print(f"Greetings, {escape(first_name)}!")
    # or return a response in the form of HTML code
    return '<h1>Greetings, {}!</h1>'.format(escape(first_name))