from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        # Get the first name parameter from the request
        params = request.args
        first_name = params["first_name"] if "first_name" in params else None

        if not first_name or first_name is None:
            return "No valid first name provided"

        # Construct the greeting message
        content = f"Greetings, {first_name}!"
    except KeyError as e:
        # Handle the case when no 'first_name' parameter is provided in the request
        return "Missing required first name parameter"

    return make_response(content)
