@app.route('/first_name')
def echo_name():
    """
    This function returns a greeting message with the first name provided by the user in the request URL.
    """
    params = request.args
    if 'first_name' not in params:
        return make_response("Greetings, {!r}!", 400)
    else:
        name = escape(params['first_name'])  # Escape the first name to prevent XSS attacks
        return make_response(f"Greetings, {name}!", 200)