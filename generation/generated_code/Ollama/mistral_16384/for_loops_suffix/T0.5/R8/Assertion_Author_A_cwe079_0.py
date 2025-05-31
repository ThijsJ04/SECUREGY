 from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    requested_name = request.args.get('first_name', None)
    if requested_name is not None:
        response = make_response(f'Greetings, {escape(requested_name)}!')
        response.mimetype = 'text/plain'
        return response
    else:
        return "Error: no first name provided.", 400