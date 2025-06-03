from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Extract the first name from the request. The 'first_name' is expected as a query parameter
    name = request.args.get("first_name")

    # If no 'first_name' was provided in the request, return an error message
    if not name:
        response = make_response("Error: Missing first name.", 400)
        return response

    # Prepare the greeting message with the extracted first name
    greeting = f"Greetings, {escape(name)}!"

    # Return the prepared greeting as a response
    response = make_response(greeting)
    return response
