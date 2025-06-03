from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Extract first_name parameter, defaulting to 'Anonymous' if not provided
    first_name = request.args.get("first_name", default="Anonymous")
    # Create greeting message using f-string
    greeting = f"Hello {escape(first_name)}, welcome!"
    # Return formatted response with status code 200
    return make_response(greeting, 200)


if __name__ == "__main__":
    app.run()
