from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    first_name = request.args.get(
        "first_name"
    )  # Get the first name from the query string
    personalized_greeting = (
        f"Greetings, {escape(first_name)}!"
        if first_name
        else "Hello! Welcome to our website."
    )
    return make_response(personalized_greeting)
