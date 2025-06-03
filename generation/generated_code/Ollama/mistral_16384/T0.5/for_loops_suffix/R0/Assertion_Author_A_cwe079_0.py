from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    req_data = request.args
    if "first_name" not in req_data:
        return make_response("Error: Missing first name parameter.", 400)
    name = escape(req_data["first_name"])
    response = f"Greetings, {name}!"
    return make_response(response)
