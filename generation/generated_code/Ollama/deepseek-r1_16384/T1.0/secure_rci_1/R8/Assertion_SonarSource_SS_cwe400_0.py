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
    # Extract regex pattern and data from query parameters
    regex = request.args.get("regex")
    data = request.args.get("data")

    # Check if both parameters are provided
    if not (regex and data):
        return "Bad request", 400

    # Search for the pattern in the data
    if re.search(regex, data):
        return "Match found"
    else:
        return "No match found"


if __name__ == "__main__":
    app.run(debug=True)
