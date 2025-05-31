@app.route('/first_name')
def echo_name():
    """Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'."""
    data = request.get_json()  # assuming the request is a JSON payload
    if not data or 'first_name' not in data:
        return make_response('No first name provided', 400)
    first_name = data['first_name']
    return make_response(f"Greetings, {first_name}!")