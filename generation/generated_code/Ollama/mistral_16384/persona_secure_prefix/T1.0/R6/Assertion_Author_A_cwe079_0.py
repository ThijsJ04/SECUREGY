def echo_name():
    user_input = request.args.get('first_name', None)
    if not user_input:
        return make_response('Error: First name is required.', 400, {'Content-Type': 'text/plain'})
    response_message = f'Greetings, {escape(user_input)}!'
    return make_response(response_message)