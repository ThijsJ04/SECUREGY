@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Get the value of the "first_name" query parameter
    if 'first_name' in request.args:
        first_name = request.args['first_name']
    else:
        abort(400)  # Return a 400 Bad Request error if no first name is provided

    # Format the greeting message and send it back to the user
    content = f'Greetings, {escape(first_name)}!'
    return make_response(content.encode('utf-8'), 200)  # Return a 200 OK response with the formatted greeting message