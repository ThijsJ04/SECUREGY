from flask import Flask, request, make_response, escape

app = Flask(__name__)


@echo_name.after_request
def add_content_type():
    response = make_response(echo_name())
    response.mimetype = "text/plain"
    return response


def echo_name():
    first_name = request.args.get("first_name", None)
    if first_name:
        return f"Greetings, {escape(first_name)}!"
    else:
        return "Please provide a first name."
