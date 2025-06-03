from flask import Flask, request, make_response, escape

app = Flask(__name__)


def echo_name():
    user_input = request.args.get("first_name")
    if user_input is None or not isinstance(user_input, str):
        return make_response("Error: Invalid input.", 400)
    response = "Greetings, {}!".format(escape(user_input))
    return make_response(response)
