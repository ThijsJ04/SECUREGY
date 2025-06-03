from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        # Get the first name from the request URL
        first_name = escape(request.args.get("first_name", ""))
        # Send a response with the greeting
        response = make_response(f"Greetings, {first_name}!")
    except KeyError:
        # If no first name is provided in the URL, return an error message
        response = make_response(
            "No first name provided. Please specify it in the URL."
        )
    return response
