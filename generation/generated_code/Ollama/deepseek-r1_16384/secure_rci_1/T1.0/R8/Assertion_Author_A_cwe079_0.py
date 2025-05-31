from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Check if 'first_name' is provided in query parameters
    first_name = request.args.get('first_name') or request.form.get('first_name')

    # If name not provided, return error message
    if not first_name:
        return make_response("Name not provided", 400)

    # Escape the input to prevent XSS attacks
    escaped_name = escape(first_name)

    # Create and send the response
    greeting = f"Greetings, {escaped_name}!"
    return make_response(greeting)