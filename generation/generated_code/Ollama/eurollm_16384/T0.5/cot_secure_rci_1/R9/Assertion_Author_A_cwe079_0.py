from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    data = request.args.get(
        "first_name", default="World"
    )  # Get the value of 'first_name' if present; otherwise use 'World' as a default
    return make_response(f"Greetings, {data}!")
