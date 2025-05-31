from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    args = request.args
    if 'first_name' not in args:
        return make_response('No first name provided', 400)
    else:
        try:
            first_name = escape(args['first_name'])  # Escape any special characters to prevent XSS attacks
            greeting = f"Greetings, {first_name}!"
        except KeyError:
            print("No first name provided")
            return make_response('No first name provided', 400)

    return make_response(greeting, 200)