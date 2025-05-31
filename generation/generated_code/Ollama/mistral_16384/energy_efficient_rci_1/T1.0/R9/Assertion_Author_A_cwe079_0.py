@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    name = request.args.get('first_name', None)
    if name is not None:
        return make_response(f"Greetings, {escape(name)}!", 200)
    else:
        return make_response("Error: First Name not found in the request.", 400)