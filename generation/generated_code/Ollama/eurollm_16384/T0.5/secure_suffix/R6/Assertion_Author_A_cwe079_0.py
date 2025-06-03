from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        # Get the first name from the request
        first_name = request.args.get("first_name")
        if not first_name:
            return make_response("Please provide a first name", 400)

        # Send back the greeting message
        greeting = f"Greetings, {escape(first_name)}!"
        return make_response(greeting)
    except ValueError:
        # Handle cases where the request is missing or malformed
        return make_response("Invalid request", 400)
