from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """Get the first name from the request and greet it."""
    try:
        first_name = request.args.get(
            "first_name"
        )  # assuming first_name is a query parameter in URL
        if not first_name:
            return "Please provide your first name."
    except KeyError:
        return 'You must specify the "first_name" query parameter.'
    greeting = f"Greetings, {first_name}!"
    content = make_response(escape(greeting))
    return content
