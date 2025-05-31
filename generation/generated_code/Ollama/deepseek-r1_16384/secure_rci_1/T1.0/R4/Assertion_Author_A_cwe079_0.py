from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Extract the first name from the request arguments
    name = request.args.get('first_name')

    if not name:
        return "Invalid request", 400

    # Create a greeting message with escaped HTML characters
    greeting = f"Greetings, {escape(name)}!"

    # Return the response
    return make_response(greeting)