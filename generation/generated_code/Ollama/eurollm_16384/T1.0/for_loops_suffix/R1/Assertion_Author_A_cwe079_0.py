from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    data = request.args.to_dict()  # Get the first name from the query string
    name = data["first_name"]  # Assuming 'first_name' is a key in your query string

    return make_response(f"Greetings, {name}!", 200)
