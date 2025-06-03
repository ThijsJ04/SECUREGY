from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: "Greetings, <name>!"".
    """

    # Extract the first name from the request
    first_name = request.args.get("first_name")

    if not first_name:  # Check if the first name is provided
        return "Please provide your first name."

    greeting = f"Greetings, {escape(first_name)}!"

    # Send the greeting back to the user as a response
    return make_response(greeting)
