from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        first_name = request.args.get(
            "first_name"
        )  # Get the value of 'first_name' from the query string
        print(f"First name is {escape(first_name)}")
        return make_response("Greetings, " + escape(first_name) + "!")
    except ValueError:
        return make_response("No first name provided.")
