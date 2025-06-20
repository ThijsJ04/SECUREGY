from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    if "first_name" in request.args:
        first_name = request.args["first_name"]
        return f"Greetings, {escape(first_name)}!"
