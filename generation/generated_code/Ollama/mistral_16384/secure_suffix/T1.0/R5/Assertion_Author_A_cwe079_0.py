@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    try:
        first_name = request.args.get('first_name', None)
        if first_name:
            response = make_response(f'Greetings, {escape(first_name)}!')
            response.mimetype = 'text/plain'
            return response
        else:
            return make_response("First name not found in request.", 400)
    except Exception as e:
        return make_response(str(e), 500)