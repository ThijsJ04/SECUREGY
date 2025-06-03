from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Extract the first_name parameter from the request arguments
    first_name = request.args.get("first_name", "")

    # Check if first_name is provided and escape special characters
    if not first_name:
        return make_response("First name required.", 400)

    greeting = f"Greetings, {escape(first_name)}!"

    # Return the response with appropriate content type
    return make_response(greeting)
