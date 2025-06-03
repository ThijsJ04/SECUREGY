from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """

    # Access the first name from the request using 'first_name'
    first_name = escape(
        request.args.get("first_name", default="World")
    )  # replace with your actual first name variable

    # Construct a greeting message with the first name
    greeting = f"Greetings, {escape(first_name)}!"

    # Return the greeting message to the user
    return make_response(
        make_response(greeting, 200)
    )  # return the greeting as a response
