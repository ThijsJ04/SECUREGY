@app.route('/first_name')
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        first_name = request.args.get('first_name').strip().lower()  # Remove whitespace from first name
        special_chars = ['"', "<",">"]  # List of special characters to be replaced by '\u2019' and '\u201C' respectively
        for char in special_chars:
            first_name = first_name.replace(char, '\\' + char)
    except ValueError:  # Handle if no name is provided or it contains only whitespace
        abort(400)

    response = make_response(f"Greetings, {first_name}!")  # Format the response with the first name
    return response.get_data()