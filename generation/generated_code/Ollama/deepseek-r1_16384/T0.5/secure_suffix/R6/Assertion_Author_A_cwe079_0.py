from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get the first name parameter from request arguments
    first_name = request.args.get("first_name", "Name not provided")

    # Escape any special characters in the response to prevent XSS attacks
    greeting = f"Greetings, {escape(first_name)}!"

    # Create and return the response object with text/plain content type
    return make_response(greeting, 200, {"Content-Type": "text/plain"})


if __name__ == "__main__":
    app.run(debug=True)
