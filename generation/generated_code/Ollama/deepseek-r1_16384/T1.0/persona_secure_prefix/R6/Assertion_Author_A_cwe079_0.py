from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    first_name = request.args.get("first_name", "")
    if not first_name:
        return make_response("First name is required.", 400)
    greetings = f"Greetings, {escape(first_name)}!"
    response = make_response(greetings)
    response.headers["Content-Type"] = "text/html; charset=utf-8"
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


if __name__ == "__main__":
    app.run(debug=True)
