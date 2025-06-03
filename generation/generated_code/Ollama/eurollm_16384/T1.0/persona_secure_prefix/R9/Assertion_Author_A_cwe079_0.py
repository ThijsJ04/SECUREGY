from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    data = request.args.get("first_name")  # Get the first name from the query string
    return f"Greetings, {data}!"  # Send back a personalized greeting to the user
