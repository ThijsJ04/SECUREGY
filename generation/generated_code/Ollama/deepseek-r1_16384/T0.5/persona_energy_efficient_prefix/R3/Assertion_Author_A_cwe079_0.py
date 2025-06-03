from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get the first name from query parameters
    name = request.args.get("first_name", "").strip()
    # Create the greeting message
    greeting = f"Greetings, {escape(name)}!"
    # Return the response with appropriate content type
    response = make_response(greeting)
    response.headers["Content-Type"] = "text/html; charset=utf-8"
    return response


if __name__ == "__main__":
    app.run(debug=True)
