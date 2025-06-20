from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    data = request.args.get("first_name", default="", type=str)
    greeting = f"Greetings, {escape(data)}!" if data else "Hello! (No name provided)"
    return make_response(greeting)
