from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Get the first name parameter from query string or form data
    first_name = request.args.get('first_name', default='', type=str)

    # If no name provided, return error response
    if not first_name:
        return make_response('Missing first_name parameter', 400)

    # Escape special characters to prevent XSS attacks
    escaped_name = escape(first_name)

    # Return the greeting message in HTML format
    response = f'<!DOCTYPE html>' \
               '<html>' \
               ' <body>' \
               f'  Greetings, {escaped_name}!' \
               ' </body>' \
               '</html>'

    return make_response(response, 200, {'Content-Type': 'text/html'})

if __name__ == '__main__':
    app.run(debug=True)