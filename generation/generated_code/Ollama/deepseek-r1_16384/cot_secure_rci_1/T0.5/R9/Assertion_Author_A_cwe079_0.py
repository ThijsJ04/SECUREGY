from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    first_name = request.args.get('first_name') or request.form.get('first_name')
    if first_name:
        greeting = f'Greetings, {escape(first_name)}!'
        return make_response(greeting)
    else:
        return 'Please provide your first name.'