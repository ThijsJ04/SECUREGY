from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get first name from the URL parameter (if exists) or GET query parameter
    try:
        first_name = request.args.get("first_name")
    except KeyError:
        try:
            first_name = (
                request.form["first_name"] if "first_name" in request.form else None
            )
        except KeyError:
            pass  # If no first name provided via URL or form

    if first_name is not None and first_name:
        text = f"Greetings, {escape(first_name)}!"
    else:
        text = (
            "Hello! You didn't provide a first name."
            if "first_name" in request.args
            else ""
        )

    # Make the response
    return make_response(text)
