from flask import Flask, request

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    # Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'
    request_data = (
        request.args.to_dict()
    )  # assuming 'first_name' is a parameter passed in the URL
    first_name = (
        request_data["first_name"] if "first_name" in request_data else "Unknown"
    )
    greeting = f"Greetings, {escape(first_name)}!"
    return make_response(greeting)
