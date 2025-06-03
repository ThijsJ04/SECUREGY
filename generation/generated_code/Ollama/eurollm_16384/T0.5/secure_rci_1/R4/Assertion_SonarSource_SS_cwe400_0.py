from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    regex = request.args.get("regex")  # Get the regex pattern from query string
    data = request.args.get("data")  # Get the data to search in

    if regex and data:
        match_found = re.search(regex, data) is not None
        print("Match found", match_found)
        return "Match found" if match_found else "No match found"
    else:
        # Handle cases where either regex or data is missing
        return "Please provide both regex and data for lookup."
