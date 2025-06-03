from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    name = request.args.get(
        "first_name", default="Guest"
    )  # If 'first_name' is not present, use the default value 'Guest'
    greeting = f"Greetings, {escape(name)}!"
    return make_response(make_response(f"Content-Type: text/html\n\n{greeting}", 200))
