from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get first_name from query parameters or form data
    first_name = request.args.get("first_name") or request.form.get("first_name")

    if not first_name:
        return make_response("First name is required.", 400)

    escaped_name = escape(first_name)
    response_message = f"Greetings, {escaped_name}!"

    return make_response(response_message, 200)


if __name__ == "__main__":
    app.run(debug=True)
