from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/greet")
def echo_name():
    first_name = request.args.get("first_name", default="World")
    return make_response(f"Greetings, {first_name}!", 200)
