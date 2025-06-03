from flask import Flask, request, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.args.get("first_name", default=None)
    personalization = (
        f"Greetings, {escape(first_name)!r}!"
        if first_name
        else "Hello! Welcome to the site."
    )
    return make_response(personalization)
