from flask import Flask, request, make_response, escape

app = Flask(__name__)


def echo_name():
    first_name = request.args.get("first_name")
    if not first_name:
        return make_response("Error: First name is required.", 400)
    response_message = f"Greetings, {escape(first_name)}!"
    return make_response(response_message)
