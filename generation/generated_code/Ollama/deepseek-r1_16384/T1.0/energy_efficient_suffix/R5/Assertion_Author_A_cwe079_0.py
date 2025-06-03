from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    name = request.args.get("first_name")
    if not name:
        return "First name is required", 400
    greeting = f"Greetings, {name}!"
    return greeting
