from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = request.args.get("regex")  # Get regex from query string
    data = request.args.get("data")  # Get data to search

    if (
        not regex or not data
    ):  # If either regex or data is missing, return 400 Bad Request
        return "Bad Request", 400

    match = re.search(regex, data)
    if match:
        return f"Match found"
    else:
        return f"No match found"
