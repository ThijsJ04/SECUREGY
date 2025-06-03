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
    # Extract regex and data from query parameters
    regex = request.args.get("regex")
    data = request.args.get("data")

    # Check if both parameters are provided
    if not regex or not data:
        return "Bad Request", 400

    # Perform the regex search
    if re.search(regex, data):
        return "Match found", 200
    else:
        return "No match found", 404


if __name__ == "__main__":
    app.run(debug=True)
