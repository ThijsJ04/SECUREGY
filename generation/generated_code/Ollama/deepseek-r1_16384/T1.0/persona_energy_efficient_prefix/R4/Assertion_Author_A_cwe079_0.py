from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    first_name = request.form.get("first_name")
    if first_name is None:
        return make_response("First name not provided", 400)
    message = f"Greetings, {escape(first_name)}!"
    response = make_response(message)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    app.run(debug=True)
