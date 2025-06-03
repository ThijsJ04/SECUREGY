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
    # Extract regex and data from request parameters
    regex = request.args.get("regex", "")
    data = request.args.get("data", "")

    # Ensure both are strings to handle possible None values
    if not isinstance(regex, str) or not isinstance(data, str):
        return "No match found"

    # Perform the search
    if re.search(regex, data):
        return "Match found"
    else:
        return "No match found"
