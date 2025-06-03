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
    data_to_search = request.args.get("data")

    if not regex_pattern or not data_to_search:
        return "Missing parameters"

    # Perform regex search
    match = re.search(regex_pattern, data_to_search)

    # Return result based on match
    return "Match found" if match else "No match found"
