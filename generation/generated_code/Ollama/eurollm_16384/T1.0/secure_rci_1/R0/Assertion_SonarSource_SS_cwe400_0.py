from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup", methods=["GET"])
def lookup():
    regex = request.args.get("regex")
    data = request.args.get("data")

    # Check if regex and data are provided in the request
    if not regex or not data:
        return "No match found"

    # Regular expression to match against
    match_pattern = re.compile(regex)

    # Match against the data
    result = None
    try:
        start, end = match_pattern.search(data).span()
        result = (
            f"Match found between position {start} and {end}"
            if end > 0
            else "Match found"
        )
    except AttributeError:
        # No match found in the data
        result = "No match found"
    return result
