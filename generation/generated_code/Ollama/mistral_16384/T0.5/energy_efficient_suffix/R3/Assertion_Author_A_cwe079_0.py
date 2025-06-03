from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Extract the first name from the request parameters
    first_name = request.args.get("first_name", None)

    if first_name is not None:  # Ensure a valid first name was provided
        response = make_response(f"Greetings, {escape(first_name)}!")
        response.headers["Content-Type"] = "text/plain"
        return response
    else:
        return make_response("Error: First name not provided.", 400)
