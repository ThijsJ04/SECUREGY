from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    name = request.args.get(
        "first_name", "Guest"
    )  # Get query parameter or default to 'Guest'
    response_text = (
        f"Greetings, {escape(name)}!"  # Escape special characters for security
    )
    return make_response(response_text)
