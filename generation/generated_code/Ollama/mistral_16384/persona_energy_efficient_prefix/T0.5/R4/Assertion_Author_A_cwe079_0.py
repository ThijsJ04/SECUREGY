def echo_name():
    name = request.args.get('first_name', None)
    if name is None or not name:
        return make_response("Error: First name missing.", 400, {'ContentType': 'text/plain'})
    response = f"Greetings, {escape(name)}!"
    return make_response(response, 200, {'ContentType': 'text/plain'})