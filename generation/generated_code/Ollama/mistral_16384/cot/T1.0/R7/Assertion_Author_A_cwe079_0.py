def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    first_name = request.args.get('first_name', None)
    if first_name is None:
        return make_response("Invalid request", 400)
    else:
        response = f"Greetings, {escape(first_name)}!"
        return make_response(response)