from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.args.get(
        "first_name"
    )  # assumes first_name is a query parameter in the URL like this: http://localhost/first_name?first_name=John
    response = make_response("Greetings, " + escape(first_name) + "!")
    return response
