from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.args.get("first_name", "Unknown")
    greeting = f"Greetings, {escape(first_name)}!"
    return make_response(greeting)
