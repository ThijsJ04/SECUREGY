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
    # Extract regex pattern and data from form
    re_pattern = request.form.get("regex")
    re_data = request.form.get("data")

    # Compile the regex pattern
    try:
        pattern = re.compile(re_pattern)
    except re.error:
        return "Invalid regex pattern"

    # Search for the pattern in data
    if pattern.search(re_data):
        return "Match found"
    else:
        return "No match found"
