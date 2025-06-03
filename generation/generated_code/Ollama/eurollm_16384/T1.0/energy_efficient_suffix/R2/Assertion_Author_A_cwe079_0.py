from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    # Get the first name from the request using 'first_name' and convert it to lowercase
    parsed_request = request.args.to_dict()
    name = parsed_request["first_name"] if "first_name" in parsed_request else None
    if name:
        # Use escape() function from Flask to replace any special characters with their HTML entities
        escaped_name = escape(name)
        return f"Greetings, {escaped_name}!"
    else:
        return "No first name provided."
