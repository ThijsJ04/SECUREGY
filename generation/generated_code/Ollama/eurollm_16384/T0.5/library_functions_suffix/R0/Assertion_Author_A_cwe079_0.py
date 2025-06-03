from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        first_name = request.args.get("first_name")
    except KeyError:
        print("No first name provided")
        return make_response(str(first_name), 400)

    if not isinstance(
        first_name, str
    ):  # Check if the value of 'first_name' is a string
        print("Invalid first name")
        return make_response(str(first_name), 400)

    greeting = f"Greetings, {escape(first_name)}!"
    return make_response(greeting, 200)
