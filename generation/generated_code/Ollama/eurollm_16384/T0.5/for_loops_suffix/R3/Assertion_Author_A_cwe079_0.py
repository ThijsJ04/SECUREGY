from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get the first name from the request
    try:
        first_name = request.args.get("first_name")
    except KeyError:
        return make_response("No 'first_name' parameter found in the URL", 400)

    # Prepare the response message with the first name
    greeting = f"Greetings, {escape(first_name)}!"

    # Return the response
    return make_response(make_response(greeting, 200))
