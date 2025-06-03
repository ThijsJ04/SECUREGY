from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name", methods=["POST"])
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    data = request.get_json()  # Assuming JSON data is sent via POST request
    if not data or "first_name" not in data:
        return make_response("Invalid Request", 400)
    first_name = escape(data["first_name"])
    greeting = f"Greetings, {first_name}!"
    return make_response(greeting.encode("utf-8"), 200)


if __name__ == "__main__":
    app.run()
