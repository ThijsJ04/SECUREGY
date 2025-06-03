from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    first_name = request.args.get(
        "first_name", default="World"
    )  # Default value if no first_name is passed in the URL
    content = f"<p>Greetings, {escape(first_name)}!</p>"
    response = make_response(content)
    return response
