from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    if "first_name" in request.args:
        name = escape(request.args.get("first_name"))
        return make_response(f"Greetings, {name}!")
    else:
        return make_response("Error: First name not found.", 400)
