from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get the first name from the request
    first_name = request.args.get("first_name", None)

    if first_name is None:
        return make_response("Missing first_name parameter", 400)

    # Prepare the response with the user's first name
    greeting = f"Greetings, {escape(first_name)}!"
    return make_response(greeting, 200)
