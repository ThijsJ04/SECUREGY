from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    if 'first_name' in request.args:
        name = escape(request.args.get('first_name'))
        response_body = f"Greetings, {name}!"
        return make_response(response_body, 200)
    else:
        error_message = "Please provide a first_name parameter."
        return make_response(error_message, 400, {
            'Content-Type': 'text/plain',
            'X-Content-Type-Options': 'nosniff'
        })