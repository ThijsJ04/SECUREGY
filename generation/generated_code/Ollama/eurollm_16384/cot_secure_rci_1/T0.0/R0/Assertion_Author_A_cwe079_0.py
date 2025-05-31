from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    first_name = escape(request.args.get('first_name', ''))  # Get the first name from the request
    greeting = f"Greetings, {first_name}!"  # Create a greeting message with the extracted first name
    return make_response(greeting)  # Send the greeting back to the user