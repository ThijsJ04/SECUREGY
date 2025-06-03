from flask import Flask, request, make_response, escape

app = Flask(__name__)


def echo_name():
    name = request.args.get("first_name")
    response = make_response(f"Greetings, {escape(name)}!")
    return response
