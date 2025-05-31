@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    if 'first_name' in request.args:
        name = request.args['first_name']
        print(f"Hello {name}")  # This line is commented for now. You need to uncomment it if you want to print the name.
        return make_response('Greetings, {}!'.format(escape(name)))
    else:
        return 'No first name provided.'