@app.route('/first_name')
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    data = request.args.get('first_name')
    if not data:
        return make_response(f'Sorry, I don\'t see a "{request.method} /first_name" parameter in your request.', 400)
    else:
        return f'Greetings, {data}!'