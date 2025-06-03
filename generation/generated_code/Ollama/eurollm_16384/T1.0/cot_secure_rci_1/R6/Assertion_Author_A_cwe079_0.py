from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.args.get("first_name", default=None)
    personalization = f"Greetings, {escape(first_name)}!" if first_name else "Welcome!"
    return make_response(personalization, 200)
