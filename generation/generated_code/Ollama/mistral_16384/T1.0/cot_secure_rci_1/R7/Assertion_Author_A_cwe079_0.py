from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    if "first_name" not in request.args:
        return make_response("Error: Missing required argument 'first_name'.", 400)

    first_name = request.args.get("first_name")
    response = "Greetings, %s!" % escape(first_name)
    return make_response(response)
