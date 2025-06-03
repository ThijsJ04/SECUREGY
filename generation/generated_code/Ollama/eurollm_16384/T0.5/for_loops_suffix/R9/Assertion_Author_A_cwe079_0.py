from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        # Get the value of the first_name parameter from the request
        data = request.args.get("first_name")
        if not data or data == "":
            return make_response("Please provide a valid first name.")

        # Ensure the user's input is properly escaped to prevent XSS attacks
        escaped_data = escape(data, quote=False)

        # Construct and return the response message
        return make_response(f"Greetings, {escaped_data}!")
    except ValueError:
        return "Invalid input. Please provide a valid first name."
