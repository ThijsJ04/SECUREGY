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
    # Try getting parameters from JSON if the content is JSON
    if request.is_json:
        payload = request.get_json()
        regex_pattern = payload.get("regex")
        input_data = payload.get("data")
    else:
        # Otherwise, get from query or form data
        regex_pattern = request.values.get("regex")
        input_data = request.values.get("data")

    if not (regex_pattern and input_data):
        return "No match found"

    if re.search(regex_pattern, input_data):
        return "Match found"
    else:
        return "No match found"
