from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    # Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    data = request.args.get("first_name")
    if not data:
        return make_response("No first name provided", 400)
    else:
        person = f"Greetings, {escape(data)}!"
        return make_response(person, 200)
