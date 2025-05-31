from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Extract the first name from query parameters
    name = request.args.get('first_name', '')

    # Create response message based on the extracted name
    if not name:
        msg = "Name not provided!"
    else:
        msg = f"Greetings, {escape(name)}!"

    # Return the formatted response
    return make_response(msg, 200, {'Content-Type': 'text/plain'})