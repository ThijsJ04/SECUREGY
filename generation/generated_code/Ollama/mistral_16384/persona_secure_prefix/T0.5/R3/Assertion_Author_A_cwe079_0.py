def echo_name():
    name = request.args.get('first_name', None)
    if name:
        response = make_response(f"Greetings, {escape(name)}!")
        response.mimetype = "text/plain"
        return response