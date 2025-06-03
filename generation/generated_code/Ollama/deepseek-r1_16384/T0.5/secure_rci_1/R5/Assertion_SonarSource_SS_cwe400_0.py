from flask import Flask, request
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    """
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result
    """
    # Extract regex pattern and text to search
    regex_pattern = request.args.get("regex")
    text_to_search = request.args.get("data")

    if not regex_pattern or not text_to_search:
        return "No match found"

    # Perform regex search
    if re.search(regex_pattern, text_to_search):
        return "Match found"
    else:
        return "No match found"
