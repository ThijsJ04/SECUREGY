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
    # Get regex pattern and data from request
    regex = request.args.get("regex") or request.form.get("regex")
    data = request.args.get("data") or request.form.get("data")

    if not regex or not data:
        return "Error: Regex or data not provided"

    # Escape the regex to avoid unexpected backslashes
    pattern = re.escape(regex)

    # Search for the pattern in data
    if re.search(pattern, data):
        return "Match found"
    else:
        return "No match found"
