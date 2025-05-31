from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    try:
        first_name = request.args.get('first_name')  # Get the value of the 'first_name' parameter from the query string
        if not first_name or len(first_name) > 256:
            return "Error! First name must be between 1 and 255 characters."
    except KeyError as e:  # Handle the case when no 'first_name' parameter is provided in the request
        return f"Error: The '{e}' parameter was not found in your query string."

    try:
        greeting = f"Greetings, {escape(first_name)}!"
        app.logger.info(f"First name received: {first_name}")
        return make_response(greeting)  # Return the greeting message as a response
    except Exception as e:  # Handle any exceptions that may occur during the execution of the function
        app.logger.error(f"Error occurred: {str(e)}")
        return "An error occurred! Please try again."