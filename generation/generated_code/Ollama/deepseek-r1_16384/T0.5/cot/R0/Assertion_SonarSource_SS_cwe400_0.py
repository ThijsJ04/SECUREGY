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
    # Extract regex pattern and data from request arguments
    regex_pattern = request.args.get("regex")
    data_str = request.args.get("data")

    if not regex_pattern or not data_str:
        return "No match found"

    try:
        if re.search(regex_pattern, data_str):
            return "Match found"
        else:
            return "No match found"
    except re.error:
        # Handle invalid regex pattern
        return "Invalid regex pattern"
