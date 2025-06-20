from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    name = request.args.get("first_name", "")
    if not name:
        return make_response("Name not provided", 400)
    greeting = f"Greetings, {escape(name)}!"
    return make_response(greeting, 200)
