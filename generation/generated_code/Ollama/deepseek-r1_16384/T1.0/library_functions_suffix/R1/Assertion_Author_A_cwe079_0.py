from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Extract first_name from query parameters
    first_name = request.args.get("first_name", default="Unknown", type=str)

    # Create greeting message
    message = f"Greetings, {escape(first_name)}!"

    # Return response
    return make_response(message)


if __name__ == "__main__":
    app.run(debug=True)
