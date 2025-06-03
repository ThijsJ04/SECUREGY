from flask import Flask, request, escape

app = Flask(__name__)


@app.route("/")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        first_name = request.args.get(
            "first_name"
        )  # Get the first name from the query parameter
        print(f"First name received: {first_name}")
    except KeyError:
        print("No 'first_name' key found in the URL.")
        return make_response(
            "No 'first_name' key found in the URL.", 400
        )  # Return a 400 Bad Request error if no first name is provided

    person = f"Greetings, {escape(first_name)}!"  # Format and escape the first name for HTML sanitization
    return make_response(
        person, 200
    )  # Return the formatted response with a 200 OK status code
