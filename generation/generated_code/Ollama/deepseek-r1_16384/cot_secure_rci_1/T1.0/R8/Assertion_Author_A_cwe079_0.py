from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Get first_name parameter from request arguments or form data
    first_name = request.args.get('first_name') if request.args else request.form.get('first_name')
    # Escape the name to prevent XSS attacks
    escaped_name = escape(first_name)
    # Create the response message
    message = f'Greetings, {escaped_name}!'
    # Return the response
    return make_response(message)