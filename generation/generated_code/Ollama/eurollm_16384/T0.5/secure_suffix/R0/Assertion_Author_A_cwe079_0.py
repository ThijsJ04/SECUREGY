from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    name = request.args.get(
        "first_name"
    )  # Assuming 'first_name' is a query parameter in the URL
    greeting = f"Greetings, {escape(name)}!" if name else "Hello there!"
    return make_response(greeting)
