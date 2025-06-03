from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    data = request.args.get(
        "first_name"
    )  # Get the first name from the URL query string (e.g., 'John')
    return make_response(f"Greetings, {data}!", 200)
