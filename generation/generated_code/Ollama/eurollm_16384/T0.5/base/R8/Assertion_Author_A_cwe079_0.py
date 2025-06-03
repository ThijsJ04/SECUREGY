from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'."""
    # Get the first name from the request
    try:
        first_name = request.args.get("first_name", default="World")
    except KeyError as e:
        abort(
            400
        )  # If no 'first_name' parameter is provided, return a 400 Bad Request error

    # Convert the first name to lowercase and escape any non-ASCII characters
    cleaned_first_name = escape(first_name).lower()

    # Format the greeting message
    greeting = (
        f"Greetings, {cleaned_first_name}!" if cleaned_first_name else "Hello World!"
    )

    # Return the greeting as a JSON response
    return make_response(json.dumps({"message": greeting}), 200)
