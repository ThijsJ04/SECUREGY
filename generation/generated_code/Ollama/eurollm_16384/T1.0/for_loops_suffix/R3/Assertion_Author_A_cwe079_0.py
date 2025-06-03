from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    request_data = request.args.to_dict()
    name = request_data[
        "first_name"
    ]  # Assuming 'first_name' is a key in the request parameters with a string value
    greeting = "Greetings, {}!".format(escape(name))
    return make_response(greeting)
