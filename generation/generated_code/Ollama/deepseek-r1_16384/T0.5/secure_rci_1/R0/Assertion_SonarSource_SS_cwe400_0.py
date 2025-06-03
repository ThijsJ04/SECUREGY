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
    # Extract regex pattern and data from the request
    regex_pattern = request.values.get("regex", "")
    data = request.values.get("data", "")

    # Compile the regex pattern
    pattern = re.compile(regex_pattern)

    # Search for the pattern in the data
    if pattern.search(data):
        return "Match found", 200
    else:
        return "No match found", 404
