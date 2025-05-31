from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Get the first name from query parameters or form data
    first_name = request.args.get('first_name', default='Unknown', type=str)

    if first_name == 'Unknown':
        # If not found in args, check form data
        first_name = request.form.get('first_name', default='Unknown', type=str)

    # Create the response message
    greeting = f'Greetings, {escape(first_name)}!'

    # Return a response with appropriate headers
    return make_response(greeting, 200, {'Content-Type': 'text/plain'})

if __name__ == '__main__':
    app.run(debug=True)