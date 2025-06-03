from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get the first name from the request arguments
    name = request.args.get("first_name")
    # Escape any special characters in the name
    escaped_name = escape(name)
    # Create the response message
    response_message = f"Greetings, {escaped_name}!"
    # Return the response using make_response to format it correctly
    return make_response(response_message)
