from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.args.get(
        "first_name", "World!"
    )  # Access first name from GET parameters or default to "World!" if not provided
    data = {"message": f"Greetings, {first_name}!"}
    return make_response(
        jsonify(data), 200
    )  # Use jsonify() for JSON response (instead of return from the view function)
