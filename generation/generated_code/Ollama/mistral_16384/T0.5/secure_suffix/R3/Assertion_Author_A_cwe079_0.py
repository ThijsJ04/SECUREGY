from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """

    # Extract the first name from the request
    name = request.args.get("first_name", None)

    if name is not None:
        # Ensure the extracted value is safe to use in output
        name = escape(name)

        # Construct and return the response
        response = make_response("Greetings, {}!".format(name))
        response.headers["Content-Type"] = "text/plain"
        return response
    else:
        # Return an error message if no first name is provided
        response = make_response("Error: First name not found.", 400)
        response.headers["Content-Type"] = "text/plain"
        return response
