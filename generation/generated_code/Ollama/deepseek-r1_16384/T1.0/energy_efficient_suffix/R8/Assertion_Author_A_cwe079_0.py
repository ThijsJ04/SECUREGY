from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Extract the first_name parameter from query arguments
    name = request.args.get("first_name", "")
    # Escape special characters to prevent XSS attacks
    escaped_name = escape(name)
    # Return a formatted string with the name
    return f"Greetings, {escaped_name}!"
