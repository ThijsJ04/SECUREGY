from flask import Flask, request

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    first_name = request.args.get("first_name")
    if not first_name:
        return "No name provided."
    greeting = f"Greetings, {escape(first_name)}!"
    return make_response(greeting)
