from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["POST"])
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    # Extract regex and data from the request
    regex = request.form.get("regex")
    data = request.form.get("data")

    # Check if both parameters are provided
    if not regex or not data:
        return "Missing parameters"

    try:
        pattern = re.compile(regex)
        match = pattern.search(data)
        if match:
            return "Match found"
        else:
            return "No match found"
    except re.error:
        return "Invalid regular expression"
