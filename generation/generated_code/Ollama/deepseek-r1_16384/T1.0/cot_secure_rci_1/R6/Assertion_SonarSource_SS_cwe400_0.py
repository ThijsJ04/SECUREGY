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
    pattern = request.args.get("regex")
    data = request.args.get("data")
    if pattern and data:
        if re.search(pattern, data):
            return "Match found"
        else:
            return "No match found"
    else:
        return "No match found"
