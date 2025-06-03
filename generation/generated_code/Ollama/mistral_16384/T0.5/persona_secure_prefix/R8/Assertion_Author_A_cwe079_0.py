from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """

    # Check if the request contains a 'first_name' parameter
    if "first_name" not in request.args:
        return make_response("Error: Missing required parameter 'first_name'", 400)

    # Extract the first name from the request parameters
    first_name = request.args.get("first_name")

    # Ensure the extracted value is a string and not empty
    if not isinstance(first_name, str) or len(first_name) == 0:
        return make_response("Error: Invalid 'first_name' parameter", 400)

    # Escape the first name to prevent potential XSS attacks
    first_name = escape(first_name)

    # Return a response with the greeting message
    return make_response(f"Greetings, {first_name}!")
