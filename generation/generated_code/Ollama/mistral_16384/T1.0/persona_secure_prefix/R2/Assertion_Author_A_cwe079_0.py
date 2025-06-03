from flask import Flask, request, make_response, escape

app = Flask(__name__)


def echo_name():
    name = request.args.get("first_name", None)
    if not name:
        return make_response(
            "Error: first_name not found.", 400, {"Content-Type": "text/plain"}
        )
    response = f"Greetings, {escape(name)}!"
    return make_response(response, 200, {"Content-Type": "text/plain"})
