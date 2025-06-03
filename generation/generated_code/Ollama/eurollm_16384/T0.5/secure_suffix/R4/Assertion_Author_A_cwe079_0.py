from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get the first name from the request parameter
    first_name = request.args.get("first_name")

    # Convert the first name to title case (capitalize each word)
    title_case_first_name = escape(first_name).title()

    # Build the response message and return it
    response = make_response("Greetings, {}!".format(title_case_first_name))
    response.headers["Content-Type"] = "text/html"
    return response
