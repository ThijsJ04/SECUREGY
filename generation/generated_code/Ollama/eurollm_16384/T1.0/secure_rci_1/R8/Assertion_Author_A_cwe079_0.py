from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    data = request.args.get("first_name")  # Assuming the GET parameter is 'first_name'
    greeting = f"Greetings, {data}!" if data else "Hello, stranger!"
    return make_response(f"{escape(greeting)}", 200)
