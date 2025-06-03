from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        first_name = request.args.get("first_name")
        print(f"First name received: {first_name}")
        response = make_response(escape(f"Greetings, {first_name}!"))
        response.headers["Content-Type"] = "text/plain; charset=UTF-8"
    except Exception as e:
        print(e)
        response = make_response("Error: Unable to retrieve first name")
    return response
