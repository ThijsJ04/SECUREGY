@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    first_name = request.args.get('first_name', default='World')  # Get the value of the 'first_name' query parameter or use a default value if not provided
    return make_response(f"Greetings, {first_name}!")