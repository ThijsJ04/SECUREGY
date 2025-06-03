from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    # Get the first name from the request URL parameters
    try:
        first_name = request.args.get("first_name")
    except ValueError:
        first_name = None

    if first_name is not None:
        greeting = f"Greetings, {first_name}!"
        return make_response(make_response(escape(greeting), 200))
    else:
        return "No name provided.", 400
