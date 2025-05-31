from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Get the first_name parameter from query string or default to empty
    first_name = request.args.get('first_name', '')

    # Escape special characters in the name to prevent XSS attacks
    escaped_name = escape(first_name)

    # Create greeting message
    greeting = f'Greetings, {escaped_name}!'

    # Return response with appropriate content type
    return make_response(greeting)