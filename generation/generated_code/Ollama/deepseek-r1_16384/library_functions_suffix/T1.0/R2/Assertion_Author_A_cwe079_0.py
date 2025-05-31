from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Get the first name from query parameters
    name = request.args.get('first_name', '')

    # Create greeting message with escaped name for safety
    message = f'Greetings, {escape(name)}!'

    # Return response with appropriate content type and message
    return make_response(message), 200