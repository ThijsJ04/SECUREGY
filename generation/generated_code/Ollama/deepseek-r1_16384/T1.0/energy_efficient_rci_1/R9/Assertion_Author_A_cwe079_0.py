from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    first_name = request.args.get("first_name")  # Get query parameter
    escaped_name = escape(first_name)  # Escape special characters
    response_message = f"Greetings, {escaped_name}!"  # Format response message
    return make_response(
        response_message
    )  # Return formatted response with proper content type
