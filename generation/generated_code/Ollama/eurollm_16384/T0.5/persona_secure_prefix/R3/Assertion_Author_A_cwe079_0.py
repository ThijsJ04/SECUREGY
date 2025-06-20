from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        first_name = request.args.get("first_name")
        print(f"First Name: {first_name}")
        greeting = f"Greetings, {first_name}!"
        response = make_response(greeting)
        return response
    except ValueError as e:
        return str(e), 400
