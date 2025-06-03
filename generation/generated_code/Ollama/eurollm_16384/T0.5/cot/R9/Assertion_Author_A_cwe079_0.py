from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        name = request.args.get("first_name")
        if not name or not isinstance(name, str):
            return make_response("Error: Missing or invalid first name", 400)
        greeting = f"Greetings, {name}!"
    except ValueError as e:
        return make_response(str(e), 500)
    return make_response(greeting, 200)
