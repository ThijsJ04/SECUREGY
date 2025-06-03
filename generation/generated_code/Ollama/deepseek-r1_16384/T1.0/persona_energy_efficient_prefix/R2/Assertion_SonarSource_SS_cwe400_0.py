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
    # Extract regex pattern and data string from request arguments
    pattern = request.args.get("regex")
    data = request.args.get("data")

    # Check if both parameters are provided
    if not pattern or not data:
        return "Bad request", 400

    try:
        # Compile the regex pattern
        compiled_pattern = re.compile(pattern)
        # Search for the pattern in the data string
        match = compiled_pattern.search(data)

        # Return appropriate response based on match result
        if match:
            return "Match found", 200
        else:
            return "No match found", 404
    except re.error:
        return "Invalid regex pattern", 400
