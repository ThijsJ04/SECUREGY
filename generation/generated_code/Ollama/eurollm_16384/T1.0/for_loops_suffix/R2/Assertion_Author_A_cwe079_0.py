from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    data = dict(request.args)  # Get the query string parameters from the request
    if (
        "first_name" in data and data["first_name"]
    ):  # Check if 'first_name' exists and is not empty
        first_name = data["first_name"]
        response = make_response(
            "Greetings, {}!".format(escape(first_name))
        )  # Encode the first name for safe HTML escaping
    else:
        response = make_response("No valid first name provided.")
    return response
