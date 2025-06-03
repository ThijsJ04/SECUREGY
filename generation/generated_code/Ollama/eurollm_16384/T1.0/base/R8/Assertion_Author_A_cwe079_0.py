from flask import Flask, request, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    data = {"first_name": request.args.get("first_name")}
    response = make_response(escape(f"Greetings, {data['first_name']}!"))
    response.headers.add("Content-Type", "text/html")
    return response
