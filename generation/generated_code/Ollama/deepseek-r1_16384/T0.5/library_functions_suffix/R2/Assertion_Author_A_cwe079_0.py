from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    name = request.args.get("first_name", "") or request.form.get("first_name", "")
    escaped_name = escape(name)
    message = f"Greetings, {escaped_name}!"
    return make_response(message, 200)


if __name__ == "__main__":
    app.run(debug=True)
