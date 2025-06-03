from flask import Flask, request, make_response, escape

app = Flask(__name__)


def echo_name():
    name = request.args.get("first_name")
    if not name:
        return make_response("Please provide a first name.", 400)
    response = f"Greetings, {escape(name)}!"
    return make_response(response)
