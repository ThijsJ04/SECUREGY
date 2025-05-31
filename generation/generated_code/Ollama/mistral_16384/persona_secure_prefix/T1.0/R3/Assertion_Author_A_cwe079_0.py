def echo_name():
    name = request.args.get('first_name', None)
    if not name:
        return make_response("Invalid request", 400)
    response = make_response(f"Greetings, {escape(name)}!")
    response.headers['Content-Type'] = 'text/plain'
    return response