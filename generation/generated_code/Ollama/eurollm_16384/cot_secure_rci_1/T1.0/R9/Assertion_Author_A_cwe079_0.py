from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    name = request.args.get('first_name', default='Guest')  # retrieve first name from query parameters
    greeting = f'Greetings, {escape(name)}!' if name else 'Welcome, Guest!'  # format greeting with escaped name or guest string
    return make_response(greeting)  # return the formatted greeting as a response