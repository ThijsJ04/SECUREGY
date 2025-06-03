from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    name = request.args.get("first_name", "")
    greeting = f"Greetings, {escape(name)}!"
    response = make_response(greeting)
    response.headers["Content-Type"] = "text/plain"
    return response
