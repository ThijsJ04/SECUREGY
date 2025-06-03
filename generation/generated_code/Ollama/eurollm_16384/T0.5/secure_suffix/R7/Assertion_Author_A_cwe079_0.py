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
        )  # Get the first name from the query string
        print(f"First Name: {first_name}")
        return make_response(escape(f"Greetings, {first_name}!"))
    except KeyError as e:
        return f"Error: Missing '{e}' parameter."
