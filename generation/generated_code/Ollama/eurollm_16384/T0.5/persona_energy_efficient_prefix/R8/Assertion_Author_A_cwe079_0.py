from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.args.get(
        "first_name"
    )  # assuming the first name is in the URL query parameter
    person = f"Greetings, {escape(first_name)}!" if first_name else "Hello!"
    return make_response(person)
