from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    name = escape(request.args.get('first_name'))  # get the value of the first_name parameter from the request and escape it for security reasons
    response = make_response(f'Greetings, {name}!')  # create a response object with the greeting message
    return response  # send the response to the user