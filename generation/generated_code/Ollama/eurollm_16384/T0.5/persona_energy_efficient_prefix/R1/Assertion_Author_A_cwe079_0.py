from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.args.get(
        "first_name"
    )  # Get the first name from the request using 'first_name'
    content = make_response(f"Greetings, {escape(first_name)}!")
    return content
