from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    name = request.args.get('first_name', '')
    escaped_name = escape(name)
    response_text = f'<h1>Greetings, {escaped_name}!</h1>'
    response = make_response(response_text)
    response.headers['Content-Type'] = 'text/html; charset=UTF-8'
    return response