@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    try:
        first_name = request.args.get('first_name')
        if not first_name or len(first_name) == 0:
            return make_response("Error: Please provide a valid value for the 'first_name' parameter.")
    except KeyError:
        return make_response("Error: The 'first_name' parameter is missing.")
    greeting = "Greetings, {}!".format(escape(first_name))
    return make_response(greeting)