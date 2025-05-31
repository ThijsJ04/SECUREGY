from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Get first_name from request arguments
    first_name = request.args.get('first_name', '')

    # Escape special characters in the greeting message
    escaped_greeting = escape(f"Greetings, {first_name}!")

    # Create response object with proper headers
    response = make_response(escaped_greeting)
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'

    return response