from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    query_string = request.args.get("first_name")
    default_greeting = "Hello there!"

    if query_string is not None:  # only use the user-provided greeting if it exists
        formatted_response = f"Greetings, {query_string}! Hello there!"
    else:  # if no first name provided, default to 'Hello there!'
        formatted_response = default_greeting

    return make_response(formatted_response)
