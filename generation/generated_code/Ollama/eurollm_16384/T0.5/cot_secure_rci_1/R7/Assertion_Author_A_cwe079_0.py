from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.args.get(
        "first_name", default="World"
    )  # get the first name from the request or use 'World' by default
    return make_response(f"Greetings, {first_name}!")
