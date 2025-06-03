from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    data = request.args.to_dict()  # Fetch all key-value pairs from the URL query string
    first_name = (
        data.get("first_name", "default").strip()
    )  # Retrieve the value associated with the 'first_name' key, and strip whitespace
    person = (
        f"Greetings, {first_name}!" if first_name else "Hello there!"
    )  # Format the response based on whether 'first_name' was found or not
    return make_response(person)
