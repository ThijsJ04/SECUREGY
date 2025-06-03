from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.args.get("first_name", "")
    if not first_name:
        return "Please provide your first name."
    greeting = "Greetings, {}!".format(escape(first_name))
    return greeting
