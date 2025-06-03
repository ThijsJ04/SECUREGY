from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    requested_name = request.args.get("first_name", None)
    if not requested_name:
        return make_response("Error: No first name provided.", 400)

    response = "Greetings, {}!".format(escape(requested_name))
    return make_response(response)
