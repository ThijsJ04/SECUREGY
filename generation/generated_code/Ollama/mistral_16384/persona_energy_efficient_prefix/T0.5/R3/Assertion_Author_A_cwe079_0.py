def echo_name():
    name = request.args.get('first_name', None)
    if name is not None:
        response = make_response(f"Greetings, {escape(name)}!")
        return response