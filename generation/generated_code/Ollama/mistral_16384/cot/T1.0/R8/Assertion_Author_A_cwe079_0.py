def echo_name():
    first_name = request.args.get('first_name', None)
    if first_name is None:
        return make_response("Error: First name not provided", 400)
    response = f"Greetings, {escape(first_name)}!"
    return make_response(response)