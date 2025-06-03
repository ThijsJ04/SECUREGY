from flask import Flask, request, make_response, escape

app = Flask(__name__)


def echo_name():
    name = request.args.get("first_name", None)
    if name is not None:
        response = make_response(f"Greetings, {escape(name)}!")
        response.mimetype = "text/plain"
        return response
