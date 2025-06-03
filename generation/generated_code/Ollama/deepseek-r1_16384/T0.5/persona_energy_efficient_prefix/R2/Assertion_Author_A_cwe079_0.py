from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.form.get("first_name") or request.args.get("first_name")
    if not first_name:
        return make_response("First name is required.", 400)
    greeting = f"Greetings, {escape(first_name)}!"
    return make_response(greeting)
