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
    pattern = re.compile(
        request.args.get("pattern")
    )  # Get the regex pattern from request parameters
    data = request.args.get("data")  # Get the data to search for the regex in

    if bool(pattern.search(data)):  # Check if the regex matches any part of the data
        return "Match found"
    else:
        return "No match found"
