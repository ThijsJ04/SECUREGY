from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    # Retrieve the first name from the request using 'first_name' and store it in a variable
    first_name = request.args.get("first_name")

    # Check if a valid first name was provided, or default to "John" if not
    if first_name:
        greeting = f"Greetings, {escape(first_name)}!"
    else:
        greeting = f"Hello, John!"

    return make_response(greeting)  # Return the greeting as a response to the user
