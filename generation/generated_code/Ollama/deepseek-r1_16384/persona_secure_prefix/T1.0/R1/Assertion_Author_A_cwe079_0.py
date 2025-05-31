from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Get first_name parameter from query string or form data
    first_name = request.args.get('first_name', default='', type=str) or \
                 request.form.get('first_name', default='', type=str)

    # Escape the name to prevent XSS attacks
    escaped_name = escape(first_name)

    # Create and return the response
    greeting = f'Greetings, {escaped_name}!'
    response = make_response(greeting)
    response.headers['Content-Type'] = 'text/plain'
    return response

if __name__ == '__main__':
    app.run()