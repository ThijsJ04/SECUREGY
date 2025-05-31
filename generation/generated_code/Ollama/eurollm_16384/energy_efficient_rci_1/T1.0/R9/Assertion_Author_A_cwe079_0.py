@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    try:
        # Get the first name from the request
        param = request.args.get('first_name')
        if not param:
            return make_response("No parameter found", 400)

        # Convert the first name to lowercase
        first_name = param.lower()

        # Build and return the response
        salutation = "Greetings, " if first_name else ""
        return make_response(salutation + first_name + "!", mimetype='text/plain')
    except Exception as e:
        return str(e)