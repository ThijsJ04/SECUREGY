from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    first_name = request.values.get('first_name', '').strip()
    if not first_name:
        return make_response('Please provide your first name.', 400)
    safe_name = escape(first_name)
    greeting = f'Greetings, {safe_name}!'
    return make_response(greeting)