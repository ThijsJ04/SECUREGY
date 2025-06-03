from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """

    # Access the first name parameter from the request object
    user_name = request.args.get("first_name")

    # Create a response with the greeting message
    response = make_response(f"Greetings, {escape(user_name)}!", 200)
    response.headers["Content-Type"] = "text/html; charset=utf-8"

    return response
