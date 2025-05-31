from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    # Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'
    try:
        first_name = request.args.get('first_name', default='World')  # If no value is provided for 'first_name', use 'World' as a fallback
    except KeyError:
        print("First name not found in query string.")
        return make_response(f"No first name provided or it was not found in the query string.", 400)

    person = f"Greetings, {escape(first_name)}!"  # Use escape to avoid any potential XSS vulnerabilities
    return make_response(person)