from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get the first name from form data
    first_name = request.form.get("first_name", "")
    # Escape special characters to prevent XSS attacks
    escaped_name = escape(first_name)
    # Create response message
    response_message = f"Greetings, {escaped_name}!"
    # Create and return a custom Response object with appropriate headers
    response = make_response(response_message)
    response.headers["Content-Type"] = "text/plain"
    response.headers["Access-Control-Allow-Origin"] = (
        "*"  # Allows all origins for simplicity
    )
    return response


if __name__ == "__main__":
    app.run(debug=True)
