from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get the first name from form data
    name = request.form.get("first_name", "")
    # Create the response message with proper escaping
    response_message = f"Greetings, {escape(name)}!"
    # Create and return the response
    response = make_response(response_message)
    response.headers["Content-Type"] = "text/plain; charset=UTF-8"
    return response


if __name__ == "__main__":
    app.run(debug=True)
