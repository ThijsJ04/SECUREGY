import re
from flask import request
from flask import Flask

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = request.args.get("regex")  # Get regex from query string
    data = request.args.get("data")  # Get data from query string

    if not regex or not data:
        return "Error: Both 'regex' and 'data' are required."

    match = re.search(regex, data)

    if match:
        return f"Match found: {data}"
    else:
        return "No match found"
