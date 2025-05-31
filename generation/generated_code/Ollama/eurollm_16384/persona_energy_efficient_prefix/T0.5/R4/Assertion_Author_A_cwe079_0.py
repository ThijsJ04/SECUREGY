@app.route('/first_name')
def echo_name():
    """Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'."""
    try:
        # Get the value of 'first_name' from the request
        data = request.args.get('first_name')
        if not data:
            return make_response("Please provide a first name", 400)

        # Convert the data to lowercase and escape any special characters
        escaped_data = escape(data).lower()

        # Return the greeting message with the escaped first name
        return make_response(f"Greetings, {escaped_data}!", 200)
    except Exception as e:
        print(e)
        return make_response("An error occurred.", 500)