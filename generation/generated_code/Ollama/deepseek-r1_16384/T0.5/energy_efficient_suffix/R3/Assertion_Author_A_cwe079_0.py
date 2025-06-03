from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    first_name = request.form.get(
        "first_name", "Guest"
    )  # Get first_name parameter with default if missing
    message = f"Greetings, {escape(first_name)}!"  # Format response and escape special characters
    return make_response(message)  # Return formatted string as response


if __name__ == "__main__":
    app.run(debug=True)
