from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Extract the first name from query parameters
    first_name = request.args.get("first_name", "")

    # Create the response message with proper escaping
    response_message = f"Greetings, {escape(first_name)}!"

    # Return the response as a properly formatted Flask response object
    return make_response(response_message)
