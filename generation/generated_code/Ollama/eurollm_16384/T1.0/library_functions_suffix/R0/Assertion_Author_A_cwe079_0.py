from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """Get the first name from the request using 'first_name' and send it back to the user in this format: "Greetings, <name>!"."""
    # Get the first name from the request
    try:
        first_name = request.args.get("first_name")
    except ValueError as e:
        return str(
            e
        ), 400  # Return a JSON error if the 'first_name' parameter is not found

    # Convert the first name to title case (capitalize each word) using Python's built-in string method
    title_case_name = first_name.title()

    # Build the greeting message and return it with a 200 status code
    greeting = f"Greetings, {escape(title_case_name)}!"
    return make_response(greeting, 200)
