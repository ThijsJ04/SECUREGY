from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    first_name = request.args.get("first_name", "")
    if not first_name:
        return make_response("Please provide a first name.", 400)
    greeting = f"Greetings, {escape(first_name)}!"
    response = make_response(greeting)
    response.headers["Content-Type"] = "text/plain"
    response.headers["Cache-Control"] = "no-cache"
    return response


if __name__ == "__main__":
    app.run(debug=True)
