from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    if request.is_json:
        first_name = request.json.get('first_name', '')
    else:
        first_name = request.values.get('first_name', '')
    greeting = f"Greetings, {escape(first_name)}!"
    response = make_response(greeting)
    response.headers['Content-Type'] = 'text/plain'
    return response