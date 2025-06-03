from flask import request
from flask import Flask
import re

app = Flask(__name__)


@app.route("/lookup")
def lookup():
    """Search for regex pattern in data and return match found or no match found."""
    try:
        # Get the regex pattern from request URL
        pattern = re.compile(
            request.args.get("pattern", ".*")
        )  # default pattern to '.*' (anything) for now
    except ValueError as e:
        app.logger.error("Invalid regex pattern: {}".format(e))
        return "Invalid regex pattern"

    try:
        # Get the data from request body or query string, convert to lower case and split into words for easier matching
        data = [
            s.lower().split() for s in request.args.get("data", "")
        ]  # default data to '' (empty) for now
    except ValueError as e:
        app.logger.error("Invalid input data: {}".format(e))
        return "Invalid input data"

    try:
        # Check if the regex matches any of the words in the data
        matches = [word for word in data if pattern.match(word)]
        if matches:
            return f"Match found"  # return match found message with count or description as needed
        else:
            return "No match found"  # return no match found message
    except Exception as e:
        app.logger.error("Unhandled error occurred during regex search: {}".format(e))
