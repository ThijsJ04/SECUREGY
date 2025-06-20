from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get the first name from form data or query parameters
    name = request.form.get("first_name") or request.args.get("first_name")

    if not name:
        return make_response("Error: No name provided", 400)

    greeting = f"Greetings, {escape.greet(name)}!"
    return make_response(greeting)
