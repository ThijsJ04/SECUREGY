from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    if "first_name" not in request.args:
        return "Error: No first name provided."
    else:
        return f"Greetings, {escape(request.args['first_name'])}!"
