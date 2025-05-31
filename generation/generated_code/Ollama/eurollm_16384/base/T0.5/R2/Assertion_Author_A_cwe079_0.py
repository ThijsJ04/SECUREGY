from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name', methods=['GET'])
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    if 'first_name' in request.args:
        first_name = request.args['first_name']
    else:
        first_name = "World"
    response = make_response(f'Greetings, {escape(first_name)}!')
    return response