from flask import Flask, request, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    first_name = request.args.get(
        "first_name", default="World"
    )  # Get the value of 'first_name' parameter (default is 'World' if not provided)
    greeting = f"Greetings, {escape(first_name)}!"  # Escape the first name to prevent XSS attacks
    return make_response(greeting)
