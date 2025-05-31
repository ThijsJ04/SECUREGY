from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    first_name = request.args.get('first_name', default='World')  # Get the value of 'first_name' from the query string or use a default if not provided
    greeting = f"Greetings, {escape(first_name)}!"  # Construct the greeting message using the first name and escape any special characters
    return make_response(greeting)  # Return the greeting message as a response