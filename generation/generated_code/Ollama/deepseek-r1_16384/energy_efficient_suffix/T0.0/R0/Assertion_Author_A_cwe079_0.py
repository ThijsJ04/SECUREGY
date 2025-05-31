from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Get the first name from query parameters or form data
    name = request.values.get('first_name', 'Anonymous')
    # Escape special characters to prevent XSS attacks
    escaped_name = escape(name)
    # Create the response message
    response_message = f'Greetings, {escaped_name}!'
    # Return the response
    return make_response(response_message)