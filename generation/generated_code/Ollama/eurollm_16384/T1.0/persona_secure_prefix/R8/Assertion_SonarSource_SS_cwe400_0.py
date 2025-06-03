import re
from flask import request
from flask import Flask

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    # Get regex pattern and data from request
    regex = request.args.get("regex")
    data = request.args.get("data")

    # Compile the regex pattern
    pattern = re.compile(regex)

    # Search for regex in data
    if not pattern.search(data):
        return "No match found"
    else:
        return "Match found"
