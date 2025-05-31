from flask import Flask, request, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    first_name = request.args['first_name']
    greeting = f'Greetings, {escape(first_name)}!'
    return make_response(greeting, 200)  # Return the greeting message with a status code of 200