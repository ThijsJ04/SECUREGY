from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    # Access first name from request using 'first_name' and send it back to the user in this format: "Greetings, <name>!"
    if "first_name" in request.args:
        first_name = request.args.get("first_name")
        safe_greeting = f"<strong><em>Greetings, {escape(first_name)}!</em></strong>"  # Use escape to prevent XSS attacks
    else:
        safe_greeting = "No first name provided!"

    response = make_response(
        safe_greeting
    )  # Create a response object with the greeting message and content-type header set to text/html
    response.headers["Content-Type"] = (
        "text/html"  # Set content type to HTML for better presentation on some browsers
    )
    return response  # Return the response (a Flask Response object) containing the greeting message
