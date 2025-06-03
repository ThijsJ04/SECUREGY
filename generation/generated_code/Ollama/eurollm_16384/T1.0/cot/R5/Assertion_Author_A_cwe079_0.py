from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.args.get(
        "first_name"
    )  # Get the first name from the request query string
    title = "Greetings, " + escape(first_name).strip() + "!" if first_name else "Hello!"
    return make_response(title)  # Send the response back to the user in HTML format
