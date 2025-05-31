from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    name = request.args.get('first_name', '')  # Get query parameter 'first_name'
    escaped_name = escape(name)  # Escape special characters for security
    response = f'Greetings, {escaped_name}!'  # Construct the response string
    return make_response(response, 200, {'Content-Type': 'text/plain'})