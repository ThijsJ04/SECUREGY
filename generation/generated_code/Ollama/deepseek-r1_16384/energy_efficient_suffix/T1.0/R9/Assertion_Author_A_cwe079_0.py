from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Get the first name from query parameters or JSON data
    first_name = request.args.get('first_name') or request.json.get('first_name')

    if not first_name:
        return make_response("Please provide a first name", 400)

    # Escape special characters to prevent XSS
    escaped_name = escape(first_name)

    # Create and return the response with the greeting message
    return make_response(f'Greetings, {escaped_name}!', 200)