from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'."""
    # Get the first name from the URL
    params = request.args
    first_name = escape(
        params["first_name"]
    )  # Escape any special characters in the first name

    # Create a response with the greeting message
    response = make_response("Greetings, " + first_name + "!")
    response.headers["Content-Type"] = (
        "text/html; charset=utf-8"  # Set the content type to HTML for better compatibility
    )
    return response
