@app.route('/first_name', methods=['GET'])
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: "Greetings, <name>!".
    """
    try:
        # Get the 'first_name' parameter from the request URL
        param = request.args.get('first_name')

        # If 'first_name' is not provided, send a 400 Bad Request response with an error message
        if not param or len(param) == 0:
            return make_response("Bad Request: First name is required", 400)

        # Create a friendly greeting message and return it as the response
        greeting = f"Greetings, {escape(param)}!"
        return make_response(make_response(str(greeting), 'text/plain'), 200)
    except ValueError:
        # If any error occurs during parsing the first name parameter, send a 400 Bad Request response with an error message
        return make_response("Bad Request: Invalid first name", 400)