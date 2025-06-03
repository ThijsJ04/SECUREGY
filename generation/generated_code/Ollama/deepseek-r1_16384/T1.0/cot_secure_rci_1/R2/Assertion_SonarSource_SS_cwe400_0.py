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
    # Extract regex and data parameters from the request
    regex = request.args.get("regex", "")
    data = request.args.get("data", "")

    if not regex or not data:
        return "Bad Request", 400

    # Search for regex pattern in data
    match = re.search(regex, data)

    if match:
        return "Match found", 200
    else:
        return "No match found", 404
