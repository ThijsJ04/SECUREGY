from flask import Flask, request

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    first_name = request.args.get("first_name")
    print(f"First Name received: {first_name}")
    if first_name is not None and len(first_name) > 0:
        return f"Greetings, {first_name}!"
    else:
        return "No first name provided."
