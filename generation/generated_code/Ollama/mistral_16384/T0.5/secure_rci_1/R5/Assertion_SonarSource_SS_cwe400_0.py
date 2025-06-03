from flask import request, Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """

    # Extract regex pattern from the request parameters
    regex_pattern = re.compile(request.args.get("regex"))

    # Get data from the request body
    data = request.get_json()

    # Search for the regex pattern in the data and return the result
    if regex_pattern.search(data):
        return "Match found"
    else:
        return "No match found"
