from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def first_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    if request.method == "GET":
        # Get the first name parameter from the query string
        params = request.args.get("first_name")

        # If a value is provided for the 'first_name' parameter, use it in the response message
        response = f"Greetings, {params}!" if params else "No first name provided."
    else:
        # If no 'first_name' parameter is provided in the request (e.g., because POST method is used), return an error message
        response = "Invalid request method"

    return make_response(escape(response))  # Render the response message with HTML tags
