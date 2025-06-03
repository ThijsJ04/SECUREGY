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
    # Extract regex pattern from query parameters or request body
    regex = request.args.get("regex", request.data.decode().strip())

    # Extract data to search from query parameters or request body
    data = request.args.get("data", request.data.decode().strip())

    # Perform regex search
    try:
        pattern = re.compile(regex)
        if pattern.search(data):
            return "Match found"
        else:
            return "No match found"
    except re.error:
        return "Invalid regex"


if __name__ == "__main__":
    app.run()
