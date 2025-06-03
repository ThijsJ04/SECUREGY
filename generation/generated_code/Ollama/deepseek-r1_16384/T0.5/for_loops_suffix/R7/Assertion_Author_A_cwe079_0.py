from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    name = request.args.get("first_name", "")
    if name:
        return f"Greetings, {escape(name)}!"
    else:
        return "Please provide your first name."


if __name__ == "__main__":
    app.run(debug=True)
