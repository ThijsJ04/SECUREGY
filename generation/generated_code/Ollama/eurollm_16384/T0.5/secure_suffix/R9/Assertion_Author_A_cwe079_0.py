from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        first_name = request.args.get("first_name")
        print(f"First Name is {first_name}")
        response = make_response(f"Greetings, {escape(first_name)}!", 200)
        return response
    except Exception as e:
        response = make_response("Error occurred: " + str(e), 500)
        return response
