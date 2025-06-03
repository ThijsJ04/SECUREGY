from flask import Flask, request, make_response, escape

app = Flask(__name__)


def echo_name():
    first_name = request.args.get("first_name", None)
    if first_name is None or len(first_name.strip()) == 0:
        return make_response("Invalid input!", 400)

    greeting = "Greetings, {}!".format(escape(first_name))
    return make_response(greeting)
