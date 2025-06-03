from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    name = escape(request.args.get("first_name", None))
    if name:
        return make_response(f"Greetings, {name}!")
    else:
        return make_response("No first name provided.", 400)
