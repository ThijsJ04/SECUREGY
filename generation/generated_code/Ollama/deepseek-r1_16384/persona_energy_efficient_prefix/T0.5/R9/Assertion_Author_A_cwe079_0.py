from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Get the first name from form data or query parameters
    first_name = request.form.get('first_name') or request.args.get('first_name')

    # If no name is provided, default to 'Anonymous'
    if not first_name:
        first_name = 'Anonymous'

    # Create the response message with proper HTML escaping
    greeting = escape.greetings_tag(first_name)

    # Return a Response object with the greeting message
    return make_response(greeting)