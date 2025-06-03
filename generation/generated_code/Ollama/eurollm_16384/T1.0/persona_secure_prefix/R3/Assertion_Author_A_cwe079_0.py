from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = (
        request.args.get("first_name")
        if "first_name" in request.args
        else request.form.get("first_name")
    )
    response = make_response(f"Greetings, {escape(first_name)}!")
    return response
