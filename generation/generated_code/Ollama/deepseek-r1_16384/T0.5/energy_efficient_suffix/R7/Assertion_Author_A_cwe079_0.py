from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get the first name parameter
    name = request.args.get("first_name", "")

    # Check if name is provided
    if not name:
        return make_response("Please provide a first name", 400)

    # Create greeting message and escape special characters
    greeting = f"Greetings, {escape(name)}!"

    # Return response with appropriate headers
    return make_response(greeting, 200)
