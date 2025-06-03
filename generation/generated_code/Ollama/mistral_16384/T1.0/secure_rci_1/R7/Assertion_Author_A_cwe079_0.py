from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    requested_first_name = request.args.get("first_name")
    if requested_first_name is None:
        return make_response("Invalid request.", 400)

    response = "Greetings, " + escape(requested_first_name) + "!"
    return make_response(response)
