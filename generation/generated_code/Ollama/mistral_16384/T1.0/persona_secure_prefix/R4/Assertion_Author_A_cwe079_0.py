from flask import Flask, request, make_response, escape

app = Flask(__name__)


def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    name = request.args.get("first_name", None)
    if name:
        response = make_response(f"Greetings, {escape(name)}!")
        response.mimetype = "text/plain"
        return response
    else:
        return make_response("First name not provided.", 400)
