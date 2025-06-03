from flask import Flask, request, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    name = request.args.get(
        "first_name", default="World"
    )  # Default value if not provided in URL
    greeting = f"Greetings, {escape(name)}!"
    return make_response(greeting)
