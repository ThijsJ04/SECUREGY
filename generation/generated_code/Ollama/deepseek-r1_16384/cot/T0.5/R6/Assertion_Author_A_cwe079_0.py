from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Get the first name from query parameters
    first_name = request.args.get('first_name', '')

    # Escape the input to prevent XSS attacks
    escaped_name = escape(first_name)

    # Create the response message
    response_message = f'Greetings, {escaped_name}!'

    # Return a Response object with the message and correct content type
    return make_response(response_message, 200, {'Content-Type': 'text/plain'})

if __name__ == '__main__':
    app.run(debug=True)