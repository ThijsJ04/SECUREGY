from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.args.get("first_name")  # get first name from request
    if not first_name or len(first_name) == 0:
        return "No first name provided!"
    greetings = f"Greetings, {escape(first_name)}!"  # create greeting with escaped text
    return make_response(greetings.encode("utf-8")).json()
