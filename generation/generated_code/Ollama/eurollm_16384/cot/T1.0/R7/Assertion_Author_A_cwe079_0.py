from flask import Flask, request, escape

app = Flask(__name__)

@app.route('/first_name', methods=['GET'])
def echo_name():
    """Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'."""

    try:
        # Retrieve the first name from the GET request parameters
        first_name = request.args['first_name']  # or any other parameter name you defined
    except KeyError as e:
        status_code = 400
        return make_response(make_response('Error', '', status=status_code), status_code)

    # Format the string to include the first name
    personalized_greeting = f'Greetings, {first_name}!' if first_name else "Welcome!"

    return make_response(make_response(personalized_greeting, 200), 200)  # or any other response status code you like