from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    first_name = request.args.get('first_name', default='World')  # Get the value of 'first_name' from the request parameters if available; otherwise, use the default value 'World'
    greeting = f"Greetings, {escape(first_name)}!"  # Use the `escape` function to safely escape any special characters in the first name before including it in the greeting string
    return make_response(greeting)  # Return the greeting as a response