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
    # Extract regex pattern and data from query parameters
    regex_pattern = request.args.get("regex", None)
    data_to_search = request.args.get("data", None)

    # Check if both parameters are provided
    if not regex_pattern or not data_to_search:
        return "Missing parameters", 400

    # Perform the search operation
    match = re.search(regex_pattern, data_to_search)

    # Return appropriate response based on match result
    if match:
        return "Match found"
    else:
        return "No match found"
