from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = request.args.get("regex")  # Get regex from query string
    data = request.args.get(
        "data", default="", type=str
    )  # Get data from query string (default to empty string if not provided)

    if regex:
        match = re.search(regex, data)
        if match:
            return "Match found"
        else:
            return "No match found"
    else:
        return "Please provide a valid regex pattern"
