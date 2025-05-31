@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    first_name = request.args.get('first_name')  # Assuming 'first_name' is a parameter in the URL or query string
    return make_response(f"Greetings, {first_name}!", 200)