from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    """Get the first name from the request and send it back to the user in this format: 'Greetings, <name>!'."""
    first_name = request.args.get('first_name', default='World')  # default value if not provided
    person = {'first_name': first_name}
    greeting = f"Greetings, {person['first_name']}!"
    response = make_response(make_response(escape(greeting), 200))
    return response