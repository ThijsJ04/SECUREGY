from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Extract first_name from query parameters or form data
    first_name = request.args.get("first_name", "") or request.form.get(
        "first_name", ""
    )

    # Validate input to prevent XSS attacks
    safe_name = escape(first_name)

    # Create response message
    message = f"Greetings, {safe_name}!"

    # Return response
    return make_response(message)


if __name__ == "__main__":
    app.run(debug=True)
