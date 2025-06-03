from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get the first name from the request
    try:
        first_name = request.args.get("first_name")
    except KeyError:
        abort(400)  # If no first name is provided, return a 400 error

    # Escape the first name to prevent XSS attacks
    escaped_first_name = escape(first_name)

    # Send back the response with the greeting
    return make_response("Greetings, " + escaped_first_name + "!")
