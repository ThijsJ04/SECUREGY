from flask import request
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    pattern = re.compile(request.args["pattern"])  # Get the regex pattern from request
    match = pattern.search(request.args["data"])  # Search for the regex in the data

    if match is None:
        return "No match found"
    else:
        print("Match found:", match.group())
        return f"Match found: {match.group()}"
