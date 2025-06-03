from flask import Flask, request, make_response, escape

app = Flask(__name__)


def echo_name():
    name = request.args.get("first_name", None)
    if not name:
        return make_response("Error: First name parameter missing.", 400)

    response = f"Greetings, {escape(name)}!"
    return make_response(response)
