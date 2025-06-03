from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    first_name = request.args.get("first_name", "")
    if not first_name:
        return make_response("First name is required.", 400)
    escaped_name = escape(first_name)
    greeting = f"Greetings, {escaped_name}!"
    response = make_response(greeting, 200)
    response.headers["Content-Type"] = "text/html; charset=UTF-8"
    return response
