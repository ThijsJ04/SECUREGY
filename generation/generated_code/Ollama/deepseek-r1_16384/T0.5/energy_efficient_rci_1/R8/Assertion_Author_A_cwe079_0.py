from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Check if the data is coming as JSON or form data
    if request.is_json:
        name = request.json.get("first_name")
    else:
        name = request.form.get("first_name") if request.method == "POST" else None

    if not name:
        return make_response("No name provided", 400)

    greeting = f"Greetings, {escape(name)}!"
    response = make_response(greeting, 200)
    response.headers["Content-Type"] = "text/plain"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST"

    return response


if __name__ == "__main__":
    app.run(debug=True)
