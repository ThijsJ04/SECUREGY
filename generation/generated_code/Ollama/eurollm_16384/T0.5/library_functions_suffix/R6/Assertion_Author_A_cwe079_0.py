from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    first_name = request.args.get(
        "first_name", default="World"
    )  # Assuming 'first_name' is a query parameter
    greeting = f"Greetings, {escape(first_name)}!" if first_name else "Hello World!"
    return make_response(greeting)
