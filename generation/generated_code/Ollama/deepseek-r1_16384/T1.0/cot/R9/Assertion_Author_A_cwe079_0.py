from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    first_name = request.args.get("first_name")
    if not first_name:
        return make_response("Please provide a first name.", 400)
    safe_name = escape(first_name)
    response_body = f"Greetings, {safe_name}!"
    return make_response(
        response_body, 200, {"Content-Type": "text/html; charset=utf-8"}
    )
