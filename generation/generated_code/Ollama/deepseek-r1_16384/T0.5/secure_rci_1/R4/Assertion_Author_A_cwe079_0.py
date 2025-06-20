from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    if "first_name" in request.args:
        name = escape(request.args["first_name"])
        response = make_response(f"{'Greetings, '}{name}!", 200)
        return response
    else:
        return make_response("Missing parameter 'first_name'", 400)
