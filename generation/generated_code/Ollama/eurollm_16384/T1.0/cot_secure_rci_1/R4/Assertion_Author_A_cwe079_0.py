from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.args.get(
        "first_name", default="World"
    )  # Get the first name from the request or use 'World' as a fallback
    greeting = f"Greetings, {escape(first_name)}!"
    return make_response(
        make_response(greeting, 200)
    )  # Create a response with the greeting and status code
