from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    name = request.args.get("first_name")  # Get the first name from the query string
    if not name:
        return make_response("Please include your first name in the URL", 400)
    content = f"Greetings, {escape(name)}!"
    return make_response(content.encode(), 200)  # Return the greeting as a response
