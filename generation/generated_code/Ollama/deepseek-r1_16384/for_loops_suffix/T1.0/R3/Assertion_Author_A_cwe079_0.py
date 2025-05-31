from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Get the first name from the request parameters
    name = request.args.get('first_name', '')
    # Create the greeting message with proper escaping
    greeting = f'Greetings, {escape(name)}!'
    # Return the response with appropriate headers
    response = make_response(greeting)
    response.headers['Content-Type'] = 'text/plain'
    return response