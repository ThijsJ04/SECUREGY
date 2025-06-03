from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    name = request.args.get("first_name", "")
    greeting = f"Greetings, {escape(name)}!"
    return make_response(greeting)


# The function retrieves the 'first_name' parameter from the request arguments,
# constructs a greeting string with proper escaping to prevent XSS,
# and returns it using Flask's make_response.
