from flask import Flask, request, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.args.get(
        "first_name", default="World"
    )  # Getting first name from query string (default to World if not provided)
    personalized_greeting = f"Greetings, {escape(first_name)}!"  # Formatting greeting with escaped first name
    return make_response(
        personalized_greeting
    )  # Returning response with personalized greeting
