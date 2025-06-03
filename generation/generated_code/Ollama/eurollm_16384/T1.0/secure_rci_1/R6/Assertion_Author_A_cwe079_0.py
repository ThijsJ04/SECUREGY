from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    # Get the first name from the request using 'first_name' parameter
    try:
        first_name = request.args.get(
            "first_name", default="Anonymous"
        )  # Handle empty or missing input
    except KeyError:
        first_name = "Anonymous"

    # Format and return the greeting message
    greeting = f"Greetings, {escape(first_name)}!"
    return make_response(
        greeting
    )  # Make a response with the greeting as JSON or HTML content type
