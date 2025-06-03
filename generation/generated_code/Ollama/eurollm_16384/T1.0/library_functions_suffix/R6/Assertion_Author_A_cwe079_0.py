from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    first_name = request.args.get(
        "first_name"
    )  # Get the value of the first_name query parameter
    sentence = f"Greetings, {escape(first_name)}!"
    response = make_response(sentence)
    response.headers["Content-Type"] = "text/plain"
    return response
