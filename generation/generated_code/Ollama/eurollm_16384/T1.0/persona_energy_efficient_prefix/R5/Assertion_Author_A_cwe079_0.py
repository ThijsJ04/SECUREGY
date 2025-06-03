from flask import Flask, request, make_response, escape

app = Flask(__name__)


def echo_name():
    first_name = request.args.get("first_name", default="World")
    title = "Greetings, {}!".format(escape(first_name))
    return make_response(title)
