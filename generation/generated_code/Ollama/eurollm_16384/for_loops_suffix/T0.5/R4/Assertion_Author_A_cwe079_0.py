from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    first_name = request.args.get('first_name', default='World')  # Get the first name from query parameters or use 'World' as a default if not provided
    personalization = f"Greetings, {escape(first_name)}!"
    return make_response(personalization)