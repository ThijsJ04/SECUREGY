from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    first_name = request.args.get(
        "first_name"
    )  # Assuming you are calling this route with a GET request
    context = {"name": first_name} if first_name else None
    return make_response(f"Greetings, {escape(first_name)}!", 200)
