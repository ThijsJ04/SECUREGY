from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    first_name = request.args.get(
        "first_name", ""
    )  # Get first_name from query parameters
    if not first_name:
        first_name = request.form.get("first_name")  # Fallback to form data
    message = f"Greetings, {escape(first_name)}!"
    return make_response(message)


if __name__ == "__main__":
    app.run(debug=True)
