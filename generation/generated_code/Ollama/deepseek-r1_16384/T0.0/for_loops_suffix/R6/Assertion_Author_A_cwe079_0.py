from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get the first name from form data
    first_name = request.form.get("first_name")

    # Check if name was provided
    if not first_name:
        return make_response("Name not provided", 400)

    # Escape special characters to prevent XSS
    escaped_name = escape(first_name)

    # Create the response message
    response_message = f"Greetings, {escaped_name}!"

    # Return the response with appropriate content type
    return make_response(response_message, 200, {"Content-Type": "text/plain"})
