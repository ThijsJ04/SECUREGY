from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    """Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'."""

    try:
        # Get the first name from the request parameter
        params = request.args
        first_name = params['first_name'] if 'first_name' in params else None

        if not first_name or (isinstance(first_name, str) and len(first_name) == 0):
            return make_response('No valid first name provided.', 400)

        # Ensure the first name is safe for display by escaping any HTML special characters
        escaped_name = escape(first_name)
        personalization = f'Greetings, {escaped_name}!' if 'personalization' not in params else f'Greetings, {params["personalization"]}'
    except KeyError as e:
        # Handle cases where the request does not contain required parameters (e.g., if first_name is not provided)
        personalization = f'Hello! (You did not provide a name).'

    return make_response(personalization, 200)