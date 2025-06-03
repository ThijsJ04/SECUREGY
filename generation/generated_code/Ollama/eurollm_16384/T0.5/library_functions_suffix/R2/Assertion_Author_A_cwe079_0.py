from flask import request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        first_name = request.args.get("first_name", default="World")
    except KeyError:
        return make_response("Missing 'first_name' query parameter", 400)

    greeting = f"Greetings, {escape(first_name)}!"
    return make_response(
        make_response(greeting, 200)
    )  # Return the greeting in JSON format with a 200 status code
