@app.route('/first_name')
def echo_name():
    # Get the first name from the request using 'first_name'
    first_name = request.args.get('first_name', default='World')

    # Send a response to the user with the greeting message
    response = make_response(f"Greetings, {escape(first_name)}!")
    return response