from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    first_name = request.args.get(
        "first_name", default="World"
    )  # Get the first name if provided in the URL
    if not first_name:
        return make_response("Please include your first name in the URL", 400)
    return f"Greetings, {escape(first_name)}!"
