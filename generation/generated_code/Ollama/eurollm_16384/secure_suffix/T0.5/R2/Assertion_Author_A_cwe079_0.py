from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        # Get the value of 'first_name' from the request parameters
        params = request.args
        if 'first_name' not in params or len(params['first_name']) == 0:
            return make_response('Please provide a first name', 400)

        # Escape any special characters in the first name to prevent XSS attacks
        sanitized_name = escape(params['first_name']).replace("'", '')

        # Send back a response with the greeting
        return make_response('Greetings, {}!'.format(sanitized_name), 200)
    except Exception as e:
        print(e)
        return make_response('An error occurred', 500)

if __name__ == '__main__':
    app.run()