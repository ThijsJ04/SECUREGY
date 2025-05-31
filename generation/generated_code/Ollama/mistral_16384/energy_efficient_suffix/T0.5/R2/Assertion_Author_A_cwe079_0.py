from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Extract the first name from the request
    name = request.args.get('first_name')

    # If no first name is provided, return an error message
    if not name:
        response = make_response("Error: First name is required.", 400)
        return response

    # Construct and return the greeting message
    greeting = f"Greetings, {escape(name)}!"
    response = make_response(greeting)
    return response