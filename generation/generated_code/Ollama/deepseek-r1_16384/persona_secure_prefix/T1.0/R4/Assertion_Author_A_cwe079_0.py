from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Get the first name from form data
    name = request.form.get('first_name', request.args.get('first_name'))

    # Escape special characters for security
    escaped_name = escape(name)

    # Create greeting message
    response_message = f'Greetings, {escaped_name}!'

    # Return the response
    return make_response(response_message)