from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get first_name parameter from request
    first_name = request.args.get("first_name")

    # Escape the input to prevent XSS attacks
    escaped_name = escape(first_name)

    # Create greeting message
    greeting = f"Greetings, {escaped_name}!"

    # Return response with appropriate content type
    response = make_response(greeting)
    response.content_type = "text/plain"
    return response


if __name__ == "__main__":
    app.run(debug=True)
