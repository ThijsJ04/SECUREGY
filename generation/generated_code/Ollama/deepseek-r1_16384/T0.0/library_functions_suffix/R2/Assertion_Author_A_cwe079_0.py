from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    first_name = request.args.get("first_name") or request.form.get("first_name")
    if not first_name:
        return make_response("First name parameter is missing", 400)
    greeting = f"Greetings, {escape(first_name)}!"
    return make_response(greeting, 200, {"Content-Type": "text/plain; charset=utf-8"})


if __name__ == "__main__":
    app.run(debug=True)
