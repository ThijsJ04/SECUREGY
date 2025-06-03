from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        # Get the first name from the request
        param = request.args.get("first_name")
        if not param:
            return make_response(f"Please provide your first name.", 400)

        # Escape any special characters in the first name to prevent XSS attacks
        escaped_param = escape(param, quote=False)

        # Send back a response with the greeting
        return make_response(f"Greetings, {escaped_param}!")
    except ValueError:
        return make_response("Invalid first name.", 400)
