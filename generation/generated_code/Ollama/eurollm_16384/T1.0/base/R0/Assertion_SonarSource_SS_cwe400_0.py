from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    data = []  # Replace this with the actual data you want to search against

    regex_input = request.args.get("regex")  # Get regex from request query parameters
    if not regex_input:
        return "No match found"

    for item in data:
        match = re.search(regex_input, item)
        if match:
            return "Match found"

    return "No match found"  # Return this if no matches are found after searching all items
