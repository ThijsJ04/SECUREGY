from flask import Flask, request, make_response, escape
app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    first_name = request.args.get('first_name', default='Anonymous')  # Get the first name from the request using 'first_name' and default to 'Anonymous' if not provided
    return make_response(f"Greetings, {escape(first_name)}!")  # Send it back to the user in this format: 'Greetings, <name>!'