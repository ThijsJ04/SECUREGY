from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    # Extract first_name parameter from query or form data
    first_name = request.args.get('first_name') or request.form.get('first_name')

    if not first_name:
        return make_response("Name not provided", 400)

    # Validate input to prevent injection attacks
    if not all(c.isalpha() or c == "'" for c in first_name):
        return make_response("Invalid name", 400)

    escaped_name = escape(first_name)
    response_message = f'Greetings, {escaped_name}!'

    return make_response(response_message)

# (The rest of your code continues as before...)