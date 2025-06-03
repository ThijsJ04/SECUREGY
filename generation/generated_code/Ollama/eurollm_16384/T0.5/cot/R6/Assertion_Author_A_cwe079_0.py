from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """

    # Access the 'first_name' parameter in the request object
    first_name = request.args.get("first_name")

    # Convert the first name to uppercase
    converted_first_name = first_name.upper()

    # Create a response message that includes the converted first name and a greeting
    response_message = f"Greetings, {converted_first_name}!"

    # Return the response as HTML content
    return make_response(f"<h1>{response_message}</h1>")
