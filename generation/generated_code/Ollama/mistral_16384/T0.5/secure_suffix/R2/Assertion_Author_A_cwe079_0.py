from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # get the first name from the request parameters
    name = request.args.get("first_name", None)

    if name is not None:  # check if first_name was provided
        response = make_response(f"Greetings, {escape(name)}!")
    else:
        response = make_response("Error: Missing 'first_name' parameter.")

    return response
