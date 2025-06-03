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
    regex_pattern = request.form.get("regex", "")
    data_to_search = request.form.get("data", "")

    if not regex_pattern or not data_to_search:
        return "Bad request", 400

    try:
        pattern = re.compile(regex_pattern)
        match = pattern.search(data_to_search)

        if match:
            return "Match found"
        else:
            return "No match found"
    except re.error:
        return "Invalid regex pattern", 400
