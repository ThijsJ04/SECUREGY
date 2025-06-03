from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get first_name parameter from query or form data
    first_name = request.values.get("first_name", "")

    if not first_name:
        return make_response(jsonify({"message": "Please provide a first name"}), 400)

    greeting = f"Greetings, {escape(first_name)}!"
    return make_response(jsonify({"message": greeting}), 200)
