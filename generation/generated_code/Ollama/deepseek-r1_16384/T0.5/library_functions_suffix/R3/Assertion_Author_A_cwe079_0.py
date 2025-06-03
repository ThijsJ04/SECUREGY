from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.args.get("first_name", "")
    escaped_name = escape(first_name)
    return f"Greetings, {escaped_name}!"
